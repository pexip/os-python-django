# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""
LANG_INFO is a dictionary structure to provide meta information about languages.

About name_local: capitalize it as if your language name was appearing
inside a sentence in your language.
The 'fallback' key can be used to specify a special fallback logic which doesn't
follow the traditional 'fr-ca' -> 'fr' fallback logic.
"""

LANG_INFO = {
    'af': {
        'bidi': False,
        'code': 'af',
        'name': 'Afrikaans',
        'name_local': 'Afrikaans',
    },
    'ar': {
        'bidi': True,
        'code': 'ar',
        'name': 'Arabic',
        'name_local': 'العربيّة',
    },
    'ast': {
        'bidi': False,
        'code': 'ast',
        'name': 'Asturian',
        'name_local': 'asturianu',
    },
    'az': {
        'bidi': True,
        'code': 'az',
        'name': 'Azerbaijani',
        'name_local': 'Azərbaycanca',
    },
    'be': {
        'bidi': False,
        'code': 'be',
        'name': 'Belarusian',
        'name_local': 'беларуская',
    },
    'bg': {
        'bidi': False,
        'code': 'bg',
        'name': 'Bulgarian',
        'name_local': 'български',
    },
    'bn': {
        'bidi': False,
        'code': 'bn',
        'name': 'Bengali',
        'name_local': 'বাংলা',
    },
    'br': {
        'bidi': False,
        'code': 'br',
        'name': 'Breton',
        'name_local': 'brezhoneg',
    },
    'bs': {
        'bidi': False,
        'code': 'bs',
        'name': 'Bosnian',
        'name_local': 'bosanski',
    },
    'ca': {
        'bidi': False,
        'code': 'ca',
        'name': 'Catalan',
        'name_local': 'català',
    },
    'cs': {
        'bidi': False,
        'code': 'cs',
        'name': 'Czech',
        'name_local': 'česky',
    },
    'cy': {
        'bidi': False,
        'code': 'cy',
        'name': 'Welsh',
        'name_local': 'Cymraeg',
    },
    'da': {
        'bidi': False,
        'code': 'da',
        'name': 'Danish',
        'name_local': 'dansk',
    },
    'de': {
        'bidi': False,
        'code': 'de',
        'name': 'German',
        'name_local': 'Deutsch',
    },
    'el': {
        'bidi': False,
        'code': 'el',
        'name': 'Greek',
        'name_local': 'Ελληνικά',
    },
    'en': {
        'bidi': False,
        'code': 'en',
        'name': 'English',
        'name_local': 'English',
    },
    'en-au': {
        'bidi': False,
        'code': 'en-au',
        'name': 'Australian English',
        'name_local': 'Australian English',
    },
    'en-gb': {
        'bidi': False,
        'code': 'en-gb',
        'name': 'British English',
        'name_local': 'British English',
    },
    'eo': {
        'bidi': False,
        'code': 'eo',
        'name': 'Esperanto',
        'name_local': 'Esperanto',
    },
    'es': {
        'bidi': False,
        'code': 'es',
        'name': 'Spanish',
        'name_local': 'español',
    },
    'es-ar': {
        'bidi': False,
        'code': 'es-ar',
        'name': 'Argentinian Spanish',
        'name_local': 'español de Argentina',
    },
    'es-mx': {
        'bidi': False,
        'code': 'es-mx',
        'name': 'Mexican Spanish',
        'name_local': 'español de Mexico',
    },
    'es-ni': {
        'bidi': False,
        'code': 'es-ni',
        'name': 'Nicaraguan Spanish',
        'name_local': 'español de Nicaragua',
    },
    'es-ve': {
        'bidi': False,
        'code': 'es-ve',
        'name': 'Venezuelan Spanish',
        'name_local': 'español de Venezuela',
    },
    'et': {
        'bidi': False,
        'code': 'et',
        'name': 'Estonian',
        'name_local': 'eesti',
    },
    'eu': {
        'bidi': False,
        'code': 'eu',
        'name': 'Basque',
        'name_local': 'Basque',
    },
    'fa': {
        'bidi': True,
        'code': 'fa',
        'name': 'Persian',
        'name_local': 'فارسی',
    },
    'fi': {
        'bidi': False,
        'code': 'fi',
        'name': 'Finnish',
        'name_local': 'suomi',
    },
    'fr': {
        'bidi': False,
        'code': 'fr',
        'name': 'French',
        'name_local': 'français',
    },
    'fy': {
        'bidi': False,
        'code': 'fy',
        'name': 'Frisian',
        'name_local': 'frysk',
    },
    'ga': {
        'bidi': False,
        'code': 'ga',
        'name': 'Irish',
        'name_local': 'Gaeilge',
    },
    'gl': {
        'bidi': False,
        'code': 'gl',
        'name': 'Galician',
        'name_local': 'galego',
    },
    'he': {
        'bidi': True,
        'code': 'he',
        'name': 'Hebrew',
        'name_local': 'עברית',
    },
    'hi': {
        'bidi': False,
        'code': 'hi',
        'name': 'Hindi',
        'name_local': 'Hindi',
    },
    'hr': {
        'bidi': False,
        'code': 'hr',
        'name': 'Croatian',
        'name_local': 'Hrvatski',
    },
    'hu': {
        'bidi': False,
        'code': 'hu',
        'name': 'Hungarian',
        'name_local': 'Magyar',
    },
    'ia': {
        'bidi': False,
        'code': 'ia',
        'name': 'Interlingua',
        'name_local': 'Interlingua',
    },
    'io': {
        'bidi': False,
        'code': 'io',
        'name': 'Ido',
        'name_local': 'ido',
    },
    'id': {
        'bidi': False,
        'code': 'id',
        'name': 'Indonesian',
        'name_local': 'Bahasa Indonesia',
    },
    'is': {
        'bidi': False,
        'code': 'is',
        'name': 'Icelandic',
        'name_local': 'Íslenska',
    },
    'it': {
        'bidi': False,
        'code': 'it',
        'name': 'Italian',
        'name_local': 'italiano',
    },
    'ja': {
        'bidi': False,
        'code': 'ja',
        'name': 'Japanese',
        'name_local': '日本語',
    },
    'ka': {
        'bidi': False,
        'code': 'ka',
        'name': 'Georgian',
        'name_local': 'ქართული',
    },
    'kk': {
        'bidi': False,
        'code': 'kk',
        'name': 'Kazakh',
        'name_local': 'Қазақ',
    },
    'km': {
        'bidi': False,
        'code': 'km',
        'name': 'Khmer',
        'name_local': 'Khmer',
    },
    'kn': {
        'bidi': False,
        'code': 'kn',
        'name': 'Kannada',
        'name_local': 'Kannada',
    },
    'ko': {
        'bidi': False,
        'code': 'ko',
        'name': 'Korean',
        'name_local': '한국어',
    },
    'lb': {
        'bidi': False,
        'code': 'lb',
        'name': 'Luxembourgish',
        'name_local': 'Lëtzebuergesch',
    },
    'lt': {
        'bidi': False,
        'code': 'lt',
        'name': 'Lithuanian',
        'name_local': 'Lietuviškai',
    },
    'lv': {
        'bidi': False,
        'code': 'lv',
        'name': 'Latvian',
        'name_local': 'latviešu',
    },
    'mk': {
        'bidi': False,
        'code': 'mk',
        'name': 'Macedonian',
        'name_local': 'Македонски',
    },
    'ml': {
        'bidi': False,
        'code': 'ml',
        'name': 'Malayalam',
        'name_local': 'Malayalam',
    },
    'mn': {
        'bidi': False,
        'code': 'mn',
        'name': 'Mongolian',
        'name_local': 'Mongolian',
    },
    'mr': {
        'bidi': False,
        'code': 'mr',
        'name': 'Marathi',
        'name_local': 'मराठी',
    },
    'my': {
        'bidi': False,
        'code': 'my',
        'name': 'Burmese',
        'name_local': 'မြန်မာဘာသာ',
    },
    'nb': {
        'bidi': False,
        'code': 'nb',
        'name': 'Norwegian Bokmal',
        'name_local': 'norsk (bokmål)',
    },
    'ne': {
        'bidi': False,
        'code': 'ne',
        'name': 'Nepali',
        'name_local': 'नेपाली',
    },
    'nl': {
        'bidi': False,
        'code': 'nl',
        'name': 'Dutch',
        'name_local': 'Nederlands',
    },
    'nn': {
        'bidi': False,
        'code': 'nn',
        'name': 'Norwegian Nynorsk',
        'name_local': 'norsk (nynorsk)',
    },
    'no': {
        'bidi': False,
        'code': 'no',
        'name': 'Norwegian',
        'name_local': 'norsk',
    },
    'os': {
        'bidi': False,
        'code': 'os',
        'name': 'Ossetic',
        'name_local': 'Ирон',
    },
    'pa': {
        'bidi': False,
        'code': 'pa',
        'name': 'Punjabi',
        'name_local': 'Punjabi',
    },
    'pl': {
        'bidi': False,
        'code': 'pl',
        'name': 'Polish',
        'name_local': 'polski',
    },
    'pt': {
        'bidi': False,
        'code': 'pt',
        'name': 'Portuguese',
        'name_local': 'Português',
    },
    'pt-br': {
        'bidi': False,
        'code': 'pt-br',
        'name': 'Brazilian Portuguese',
        'name_local': 'Português Brasileiro',
    },
    'ro': {
        'bidi': False,
        'code': 'ro',
        'name': 'Romanian',
        'name_local': 'Română',
    },
    'ru': {
        'bidi': False,
        'code': 'ru',
        'name': 'Russian',
        'name_local': 'Русский',
    },
    'sk': {
        'bidi': False,
        'code': 'sk',
        'name': 'Slovak',
        'name_local': 'slovenský',
    },
    'sl': {
        'bidi': False,
        'code': 'sl',
        'name': 'Slovenian',
        'name_local': 'Slovenščina',
    },
    'sq': {
        'bidi': False,
        'code': 'sq',
        'name': 'Albanian',
        'name_local': 'shqip',
    },
    'sr': {
        'bidi': False,
        'code': 'sr',
        'name': 'Serbian',
        'name_local': 'српски',
    },
    'sr-latn': {
        'bidi': False,
        'code': 'sr-latn',
        'name': 'Serbian Latin',
        'name_local': 'srpski (latinica)',
    },
    'sv': {
        'bidi': False,
        'code': 'sv',
        'name': 'Swedish',
        'name_local': 'svenska',
    },
    'sw': {
        'bidi': False,
        'code': 'sw',
        'name': 'Swahili',
        'name_local': 'Kiswahili',
    },
    'ta': {
        'bidi': False,
        'code': 'ta',
        'name': 'Tamil',
        'name_local': 'தமிழ்',
    },
    'te': {
        'bidi': False,
        'code': 'te',
        'name': 'Telugu',
        'name_local': 'తెలుగు',
    },
    'th': {
        'bidi': False,
        'code': 'th',
        'name': 'Thai',
        'name_local': 'ภาษาไทย',
    },
    'tr': {
        'bidi': False,
        'code': 'tr',
        'name': 'Turkish',
        'name_local': 'Türkçe',
    },
    'tt': {
        'bidi': False,
        'code': 'tt',
        'name': 'Tatar',
        'name_local': 'Татарча',
    },
    'udm': {
        'bidi': False,
        'code': 'udm',
        'name': 'Udmurt',
        'name_local': 'Удмурт',
    },
    'uk': {
        'bidi': False,
        'code': 'uk',
        'name': 'Ukrainian',
        'name_local': 'Українська',
    },
    'ur': {
        'bidi': True,
        'code': 'ur',
        'name': 'Urdu',
        'name_local': 'اردو',
    },
    'vi': {
        'bidi': False,
        'code': 'vi',
        'name': 'Vietnamese',
        'name_local': 'Tiếng Việt',
    },
    'zh-cn': {
        'fallback': ['zh-hans'],
        'bidi': False,
        'code': 'zh-cn',
        'name': 'Simplified Chinese',
        'name_local': '简体中文',
    },
    'zh-hans': {
        'bidi': False,
        'code': 'zh-hans',
        'name': 'Simplified Chinese',
        'name_local': '简体中文',
    },
    'zh-hant': {
        'bidi': False,
        'code': 'zh-hant',
        'name': 'Traditional Chinese',
        'name_local': '繁體中文',
    },
    'zh-hk': {
        'fallback': ['zh-hant'],
    },
    'zh-mo': {
        'fallback': ['zh-hant'],
    },
    'zh-my': {
        'fallback': ['zh-hans'],
    },
    'zh-sg': {
        'fallback': ['zh-hans'],
    },
    'zh-tw': {
        'fallback': ['zh-hant'],
        'bidi': False,
        'code': 'zh-tw',
        'name': 'Traditional Chinese',
        'name_local': '繁體中文',
    },
}
