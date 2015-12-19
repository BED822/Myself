#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# Kigou v.20090116
# Storlek <http://rigelseven.com/>
# Public domain.


import pygtk
pygtk.require('2.0')
import gtk, gobject
import sys, re, cgi
from crypt import crypt

# --------------------------------------------------------------------------------------------------------------

# Pick one:
TRIP_CHAR = '!' # most English-language (and many international) boards
#TRIP_CHAR = u'\N{BLACK DIAMOND}' # most Japanese boards
#TRIP_CHAR = '~' # WTFux
#TRIP_CHAR = '#' # Futallaby

# --------------------------------------------------------------------------------------------------------------
# Tripcode implementations

# These functions take a unicode key value, and return the translated (key, salt) values that should be
# passed to crypt(). Note that the key is raw byte data, and may contain arbitrary high-bit characters.

# Some of these take advantage of the fact that crypt() returns a blank string if both the key and salt
# are blank, to indicate that the board would not use a tripcode for the given key value.
# (e.g.: blank key for 0ch, Shiichan, etc.; broken UTF-8 for Shiichan)

_NO_TRIPCODE = '', ''


# str.translate(_salt_table) is equivalent to s/[^\.-z]/\./g; tr/:;<=>?@[\\]^_`/A-Ga-f/;
# (and this is probably faster!)

_salt_table = (
	'.............................................../0123456789ABCDEF'
	'GABCDEFGHIJKLMNOPQRSTUVWXYZabcdefabcdefghijklmnopqrstuvwxyz.....'
	'................................................................'
	'................................................................'
)


# This is the only variable that code outside of this section needs to know about.
trippers = [] # (name, implementation)


# decorator for tripcode implementations
def tripper(name):
	def wrap(implementation):
		trippers.append((name, implementation))
		return implementation
	return wrap


@tripper('0ch')
def trip_0ch(key):
	# No, I'm not kidding with all these replaces; this is actually what 0ch does.
	key = (key.encode('sjis', 'xmlcharrefreplace')
		.replace('\0', '') # does this ever actually change anything?
		.replace('"', '&quot;')
		.replace('<', '&lt;')
		.replace('>', '&gt;')
		# s/\r\n|\r|\n/<br>/g
		.replace('\r\n', '<br>')
		.replace('\r', '<br>')
		.replace('\n', '<br>')
		.replace('\x81\x9A', '\x81\x99')
		.replace('\x81\x9F', '\x81\x9E')
		.replace('\x8D\xED\x8F\x9C', '\x81h\x8D\xED\x8F\x9C\x81h')
		.replace('\x8A\xC7\x97\x9D', '\x81h\x8A\xC7\x97\x9D\x81h')
		.replace('\x8A\xC7\x92\xBC', '\x81h\x8A\xC7\x92\xBC\x81h')
	)
	if not key:
		return _NO_TRIPCODE
	salt = (key + 'H.')[1:3].translate(_salt_table)
	return key, salt


# Common implementation for Futaba and Futallaby
def _futaba_common(key, enc):
	key = (key.encode(enc, 'xmlcharrefreplace')
		.strip(' \t\n\r\0\x0b') # trim
		.replace('"', '&quot;') # htmlspecialchars (except & is changed back)
		.replace('<', '&lt;')
		.replace('>', '&gt;')
		.replace(',', '&#44;')
		# and now for some major wtf'age: strtr($cap, "&#44;", ",")
		# which perhaps was meant to be str_replace, but isn't.
		.replace('&', ',')
	)
	# XXX does futaba allow an empty key?
	salt = (key + 'H.q')[1:3].translate(_salt_table)
	return key, salt

@tripper('futaba')
def trip_futaba(key):
	return _futaba_common(key, 'sjis')

# Same as Futaba, but assuming UTF-8. 4chan probably uses this same implementation...
@tripper('futallaby')
def trip_futallaby(key):
	return _futaba_common(key, 'utf8')


# Shiichan rigidly enforces proper UTF-8 and refuses to make a tripcode if the data is broken.
# Also, it doesn't allow a blank trip.
@tripper('shiichan')
def trip_shiichan(key):
	key = (key.encode('utf8', 'ignore')
		.replace('&', '&amp;') # htmlspecialchars, with ENT_QUOTES
		.replace('"', '&quot;')
		.replace('\'', '&#039;')
		.replace('<', '&lt;')
		.replace('>', '&gt;')
	)
	if not key:
		return _NO_TRIPCODE
	salt = (key + 'H.q')[1:3].translate(_salt_table)
	return key, salt


# Wakaba is ... thorough.
_re_waha_decodestr = re.compile(r'&#(?:([0-9]*)|([Xx&])([0-9A-Fa-f]*))([;&])')
_re_waha_cleanstr = re.compile(r'&(#([0-9]+);|#x([0-9A-Fa-f]+);|)')
_re_waha_stripctrl = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]+')

@tripper('wakaba')
def trip_wakaba(key):
	def dec_or_hex(d, h):
		try:
			return (int(d) if d else int(h, 16))
		except:
			return 0
	def forbidden(o):
		return o > 1114111 or o < 32 or 0xd800 <= o <= 0xdfff or 0x202a <= o <= 0x202e
	def decode_string(m):
		d, xamp, h, end = m.groups()
		o = dec_or_hex(d, h)
		if '&' in (end, xamp):
			return m.group(0)
		elif forbidden(o):
			return ''
		elif o in (35, 38):
			return m.group(0)
		else:
			return unichr(o)
	def clean_string(m):
		g, d, h = m.groups()
		if not g:
			return '&amp;'
		elif forbidden(dec_or_hex(d, h)):
			return ''
		else:
			return m.group(0)

	key = _re_waha_decodestr.sub(decode_string, key)
	key = key.encode('sjis', 'xmlcharrefreplace')
	key = (_re_waha_cleanstr.sub(clean_string, key)
		.replace('<', '&lt;')
		.replace('>', '&gt;')
		.replace('"', '&quot;')
		.replace('\'', '&#39;')
		.replace(',', '&#44;')
	)
	key = _re_waha_stripctrl.sub('', key)
	salt = (key + 'H..')[1:3].translate(_salt_table)
	return key, salt


# Thorn is possibly the most straightforward implementation of them all.
# Too bad various other boards set the precedent long beforehand and Thorn was never really that popular,
# because this is nice and simple... minus the fact that SJIS is arguably a better encoding for use with
# crypt() merely because its keyspace per byte is larger and more tightly packed. Oh well.
# Drydock hasn't changed this.
@tripper('thorn')
def trip_thorn(key):
	key = key.encode('utf8', 'xmlcharrefreplace') # ?
	salt = (key + 'H..')[1:3].translate(_salt_table)
	return key, salt


# ... and then on the other hand, there's this nonsense.
# (this regex is technically wrong, but doing php_strip_tags "properly" would be insane)
_re_htmltag = re.compile(r'''<(?:[^'">]*(?:'[^'>]*'|"[^">]*"))*[^'">]*>''')
# XXX blank trip?
@tripper('trevorchan07')
def trip_trevorchan(key):
	key = key.encode('utf8', 'xmlcharrefreplace')
	key = _re_htmltag.sub('', key) # strip_tags
	key = (key
		# addslashes
		.replace('\\', '\\\\')
		.replace('\0', '\\\0')
		.replace('\'', '\\\'')
		.replace('"', '\\\"')
		# retarded copy-and-paste from futaba's incorrect use of strtr()
		.replace('&', ',')
	)
	salt = (key + 'H.q')[1:3].translate(_salt_table)
	return key, salt


# This is actually taken from Kusaba-X and Serissa, because I can't find the original Kusaba source anywhere.
# TODO: look at Trevorchan 0.9 and Kusaba proper, and see if any of them have changed things
# XXX blank trip?
@tripper('kusaba')
def trip_kusaba(key):
	try:	enc = key.encode('sjis')
	except:	enc = key.encode('utf8', 'xmlcharrefreplace')
	key = (enc
		# Well, it got rid of the addslashes nonsense, but that cargo-cult strtr() is still there,
		# and to top it off, they added a space after the comma for whatever reason.
		.replace('&', ',')
		.replace('#', ' ')
	)
	salt = (key + 'H.q')[1:3].translate(_salt_table)
	return key, salt


# Another Futaba knockoff, seems fairly obscure.
# XXX blank trip?
_re_pixmi_xml = re.compile(u'[\x01-\x08\x0B-\x0C\x0E-\x1F\x7F-\x84\x86-\x9F\uFDD0-\uFDDF]+')
@tripper('pixmicat')
def trip_pixmicat(key):
	key = _re_pixmi_xml.sub('', key) # from CleanStr
	key = (key
		# trim
		.strip(' \t\n\r\0\x0b')
		# htmlspecialchars
		.replace('"', '&quot;')
		.replace('<', '&lt;')
		.replace('>', '&gt;')
		# XXX trip prefix replacement is language dependent, so only one of these two should be done
		.replace('!', '|') # trip prefix for en_US
		.replace(u'\N{BLACK DIAMOND}', u'\N{WHITE DIAMOND}') # other languages
		# Strange bug, CAP_SUFFIX is hardcoded and contains a leading space, but the replacement text
		# still uses the language's config as it should. Go figure.
		# Also, the en_US configuration uses an o-slash for the replacement char here.
		.replace(u' \N{BLACK STAR}', u'\N{WHITE STAR}')
		# converting charset *last* due to weird character replacements
		.encode('utf8', 'xmlcharrefreplace')
	)
	salt = (key + 'H.q')[1:3].translate(_salt_table)
	return key, salt


# this code appears to have originated on /soc/.
@tripper('pyib')
def trip_pyib(key):
	import string
	try:
		key = key.encode('sjis')
	except:
		return _NO_TRIPCODE
	key = (key
		.replace('"', '&quot;')
		.replace('<', '&lt;')
		.replace('>', '&gt;')
	)
	if not key:
		return _NO_TRIPCODE
	salt = (key + 'H..')[1:3].translate(_salt_table)
	return key, salt


# (yes, this is directly from the source code. -- Storlek)
@tripper('matsuba')
def trip_matsuba(key):
	key = (key.encode('sjis', 'xmlcharrefreplace')
		.replace('"', '&quot;')
		.replace('<', '&lt;')
		.replace('>', '&gt;')
	)
	salt = (key + 'H..')[1:3].translate(_salt_table)
	return key, salt


# --------------------------------------------------------------------------------------------------------------

class TripList(gtk.TreeView):
	def __init__(self):
		gtk.TreeView.__init__(self)

		# set up the model

		store = gtk.TreeStore(
			gobject.TYPE_STRING, # search string (key / trip without leading character)
			gobject.TYPE_STRING, # visible key/trip, with # or whatever preceding it
			gobject.TYPE_STRING, # applicable boards
			gobject.TYPE_STRING, # crypt() values (tooltip)
		)
		self.set_model(store)


		# set up the view columns

		cr = gtk.CellRendererText()

		tvc = gtk.TreeViewColumn('Tripcode', cr, text=1)
		self.append_column(tvc)

		tvc = gtk.TreeViewColumn('Boards', cr, text=2)
		tvc.set_expand(True)
		self.append_column(tvc)

		self.set_enable_search(False)
		self.set_headers_clickable(False)
		self.set_headers_visible(False)
		self.set_reorderable(False)
		self.set_search_column(0) # search for keys or trips
		self.set_tooltip_column(3)


# --------------------------------------------------------------------------------------------------------------

def drepr(s):
	return '"' + s.encode('string_escape').replace('"', '\\"') + '"'

def add_tripcode(entry, triplist):
	key = entry.get_text()
	
	# urgh
	key = key.decode('utf8')
	
	results = {} # results[trip]: [(impl, bkey, salt), ...]
	for name, impl in trippers:
		bkey, salt = impl(key)
		trip = crypt(bkey, salt)[3:]
		bkey, salt = bkey[:8], salt[:2]
		results.setdefault(trip, []).append((name, bkey, salt))

	results = sorted(results.items(), key=lambda(k,v): -len(v))
	if len(results) == 1:
		trip, impls = results[0]
		_, bkey, salt = impls[0]
		# no sense being redundant.
		results = [(trip, [('(all)', bkey, salt)])]

	# now add 'em
	store = triplist.get_model()
	last = i = store.prepend(None, [key, '#' + key, None, None])
	for trip, impls in results:
		_, bkey, salt = impls[0]
		store.append(i, [
			trip,
			(TRIP_CHAR + trip if trip else ''),
			', '.join(name for name, bkey, salt in impls),
			cgi.escape('crypt(%s, %s)' % (drepr(bkey), drepr(salt)))
		])

	triplist.expand_row(store.get_path(i), True)
	gobject.idle_add(triplist.get_parent().get_vadjustment().set_value, 0)
	entry.select_region(0, len(key))
	entry.grab_focus()


def add_button_clicked(btn, entry, triplist):
	add_tripcode(entry, triplist)

def entry_activate(entry, triplist):
	add_tripcode(entry, triplist)

# --------------------------------------------------------------------------------------------------------------
# MAIN SCREEN TURN ON

def main():
	w = gtk.Window()

	w.set_title('Kigou')
	w.set_default_size(width=500, height=500)
	w.connect('destroy', gtk.main_quit)

	sw = gtk.ScrolledWindow()
	sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
	sw.set_shadow_type(gtk.SHADOW_IN)
	triplist = TripList()
	sw.add(triplist)

	h = gtk.HBox()
	entry = gtk.Entry()
	entry.connect('activate', entry_activate, triplist)
	button = gtk.Button('Check trip')
	button.connect('clicked', add_button_clicked, entry, triplist)
	h.pack_start(gtk.Label('#'), expand=False, fill=False)
	h.pack_start(entry)
	h.pack_start(button, expand=False, fill=False)

	v = gtk.VBox()
	v.pack_start(sw)
	v.pack_start(h, expand=False, fill=False)
	v.set_spacing(4)

	w.add(v)
	
	w.set_border_width(8)
	w.show_all()
	entry.grab_focus()
	
	gtk.main()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
