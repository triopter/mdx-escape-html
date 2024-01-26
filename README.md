# mdx-escape-html

Python-markdown extension to escape HTML in raw markdown.  

If you're using markdown because you want to bebable to sanitize user input, you really don't want your users to be able to embed HTML in markdown.  Bleach is great for stripping HTML, but if you run it after rendering markdown to HTML (which is the default in most tools), it overdoes the cleaning.  So for instance, if you use an extension to add `target="_blank"` to all links, you have two options:

  * Configure Bleach to disallow links or the `target` attr in HTML.  It will then strip all links / target attrs, including clean and valid ones rendered from markdown.
  * Configure Bleach to allow links and the `target` attr in HTML.  Bleach will then allow the user to entire `<a target="_self">`, which is counter-productive.
  
This extension solves this problem per the suggested method in the [python-markdown v3.0 changelog](https://python-markdown.github.io/changelog/#safe_mode-and-html_replacement_text-keywords-deprecated), by disabling the preprocessor and pattern that render HTML, and causing HTML to be escaped (ex: `<` => `&lt;`).

Compatible with Python-markdown v3.
