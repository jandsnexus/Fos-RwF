import re, pathlib
html = pathlib.Path('index.html').read_text(encoding='utf-8')
css  = pathlib.Path('style.css').read_text(encoding='utf-8')
js   = pathlib.Path('app.js').read_text(encoding='utf-8')

# Inline CSS: replace <link rel="stylesheet" href="style.css"> with <style>…</style>
html = re.sub(
    r'<link rel="stylesheet" href="style\.css">',
    '<style>\n' + css + '\n  </style>',
    html
)
# Inline JS: replace <script src="app.js"></script> with inline script.
# Guard against an accidental </script> inside the JS (there is none, but be safe).
assert '</script>' not in js, "app.js contains </script> — needs escaping"
html = re.sub(
    r'<script src="app\.js"></script>',
    '<script>\n' + js + '\n  </script>',
    html
)
pathlib.Path('fos-dashboard.html').write_text(html, encoding='utf-8')
print('built fos-dashboard.html', len(html), 'bytes')
