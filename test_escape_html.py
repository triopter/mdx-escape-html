import markdown
import pytest


def _mark_down(md_str):
    return markdown.markdown(md_str, extensions=['mdx_escape_html'])

def test_generated_html():
    md = _mark_down('foo bar')
    assert md =='<p>foo bar</p>'
    
def test_existing_html():
    md = _mark_down('foo <span class="whatever">bar</span> baz')    
    assert md =='<p>foo &lt;span class="whatever"&gt;bar&lt;/span&gt; baz</p>'
    
    
    