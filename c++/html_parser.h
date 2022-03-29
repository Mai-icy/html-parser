#include <iostream>
#include <regex>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <fstream>

class HtmlFile;

class Element
{
public:
    Element(const std::string &node_txt);
    ~Element();

    Element *operator[](int index) const { return child_nodes[index]; };

    Element *nextNode() const { return next_node; };
    Element *firstChild() const { return child_nodes.size() ? child_nodes[0] : nullptr; };
    Element *lastChild() const { return child_nodes.size() ? child_nodes[child_nodes.size() - 1] : nullptr; };

    std::string getAttribute(const std::string &key) const;
    Element *parentNode() const { return parent_node; };
    std::string nodeName() const { return node_name_; };
    std::string nodeValue() const { return node_value_; };
    const std::vector<Element *> &childNodes() const { return child_nodes; };

    friend HtmlFile;

private:
    Element *parent_node;
    Element *next_node;
    std::string node_name_;
    std::string node_value_;
    std::vector<Element *> child_nodes;
    std::map<std::string, std::string> attribute_map;

    void parseAttribute(const std::string &node_txt);
    static std::string getNodeName(const std::string &node_txt);
};

class HtmlFile
{
public:
    HtmlFile(const std::string &path) { openFile(path); };
    ~HtmlFile() { delete root_node; };

    void openFile(const std::string &path);

    Element *getElementById(const std::string &id);
    const std::vector<Element *> &getElementByTagName(const std::string &tag_name);
    const std::vector<Element *> &getElementByClassName(const std::string &class_name);

private:
    Element *root_node = new Element("root");

    void main_parse(const std::string &ori_txt);

    std::map<std::string, Element *> element_id_map;
    std::map<std::string, std::vector<Element *>> element_tag_name_map;
    std::map<std::string, std::vector<Element *>> element_class_name_map;
};
