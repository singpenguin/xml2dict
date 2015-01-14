#!/usr/bin/env python
# encoding:utf-8

from lxml import etree


def parse(xml_str):
    xml = etree.XML(xml_str)
    nsmap = xml.nsmap.values()
    nsmap = ["{"+x+"}" for x in nsmap]

    tag = _del_xmlns(nsmap, xml.tag)
    dic = {tag: []}
    _xml2dict(xml, dic[tag], nsmap)
    return dic

def _del_xmlns(xmlns, tag):
    for x in xmlns:
        if x in tag:
            return tag.replace(x, "")
    return tag

def _xml2dict(node, res, xmlns):
    rep = {}

    tag = _del_xmlns(xmlns, node.tag)
    if len(node):
        for x in list(node):
            tag_x = _del_xmlns(xmlns, x.tag)
            rep[tag] = []
            value = _xml2dict(x, rep[tag], xmlns)

            if len(x):
                value = {"value":rep[tag], "attr":x.attrib}
                res.append({tag_x:value})
            else:
                res.append(rep[tag][0])
    else:
        value = {}
        value = {"value":node.text.strip(), "attr":node.attrib}
        res.append({tag:value})
    return

if __name__ == "__main__":
    xml_str = """
    <mydocument has="an attribute">
        <and>
            <many>elements</many>
            <many>more elements</many>
        </and>
        <plus a="complex">
            element as well
        </plus>
    </mydocument>
    """
    print(parse(xml_str))
