from markdown.extensions import Extension


class EscapeHtml(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.deregister("html_block")
        md.inlinePatterns.deregister("html")


def makeExtension(*args, **kwargs):
    return EscapeHtml(*args, **kwargs)
