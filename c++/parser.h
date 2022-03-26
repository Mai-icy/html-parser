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
    std::map<std::string, std::string> attribute_map;
    std::vector<Element *> derive_ele_vector;
    void parse_attribute(const std::string &tag_txt);

public:
    Element(const std::string &tag_txt, const std::string &value);
    void add_derive_ele(Element *new_ele) { derive_ele_vector.push_back(new_ele); };
    void set_parent(Element *parent_ele) { parent_ = parent_ele; };
    const Element *parent() const { return parent_; };
    const std::vector<Element *> derive_elements() const;
    std::string tag() const {return tag_;};
    std::string get_attribute(std::string key) const;
    void show();
};

std::string get_tag_type(const std::string &tag_text);
std::string::const_iterator search_element(const std::string &text);
std::string read_html(const std::string &html_path);
void parse_ml(const std::string &ori_text);
