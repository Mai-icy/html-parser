#include <iostream>
#include <regex>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <fstream>

class Element
{
private:
    Element *parent_;
    std::string tag_;
    std::string value_;
    std::vector<Element *> derive_ele_vector;
    std::map<std::string, std::string> attribute_map;
    std::string get_tag_type(const std::string &tag_text);
    void parse_attribute(const std::string &tag_txt);
    void set_parent(Element *parent_ele) { parent_ = parent_ele; };
    void add_derive_ele(Element *new_ele) { derive_ele_vector.push_back(new_ele); };

public:
    Element(const std::string &tag_txt);
    ~Element();
    const Element *parent() const { return parent_; };
    const std::vector<Element *> &derive_elements() const { return derive_ele_vector; };
    std::string tag() const { return tag_; };
    std::string get_attribute(std::string key) const;
    void show();

    friend HtmlFile;
};

std::string get_tag_type(const std::string &tag_text);
std::string::const_iterator search_element(const std::string &text);
std::string read_html(const std::string &html_path);
void parse_ml(const std::string &ori_text);

class HtmlFile
{
private:
    Element top_ele;
    void main_parse(const std::string &ori_text);

public:
    HtmlFile(const std::string &path);
};
