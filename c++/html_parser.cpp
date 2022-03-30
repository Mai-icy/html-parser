#include "html_parser.h"

Element::Element(const std::string &node_txt) : parent_node(nullptr), next_node(nullptr)
{
    parseAttribute(node_txt);
}
Element::~Element()
{
    for (Element *&child_node : child_nodes)
    {
        delete child_node;
    }
}
std::string Element::getAttribute(const std::string &key) const
{
    auto iter = attribute_map.find(key);
    return iter != attribute_map.end() ? iter->second : "";
}
std::string Element::getNodeName(const std::string &node_txt)
{
    using namespace std;
    smatch result;
    regex type_reg("([^=\\s]*)");
    auto ret = regex_search(node_txt.cbegin(), node_txt.cend(), result, type_reg);
    return ret ? result.str(1) : "";
}
void Element::parseAttribute(const std::string &node_txt)
{   
    using namespace std;
    cout<< node_txt<<endl;
    node_name_ = getNodeName(node_txt);
    regex words_regex("(\\S*)[\\s]*=[\\s]*['\"]([^>\\s]*)['\"]");
    auto words_begin = sregex_iterator(node_txt.cbegin(), node_txt.cend(), words_regex);
    auto words_end = sregex_iterator();
    for (sregex_iterator k = words_begin; k != words_end; ++k)
    {
        smatch match = *k;
        string attr = match.str(1);
        string value = match.str(2);
        attribute_map[attr] = value;
        // cout << attr << ":的值:" << value << endl;
    }
}
void Element::setParent(Element *parent_ele)
{
    parent_node = parent_ele;
    parent_ele->child_nodes.push_back(this);
}
std::ostream &operator<<(std::ostream &os, const Element &ele)
{
    os << ele.nodeName();
    return os;
}

void HtmlFile::addClassTagMap(std::string key, Element *temp, std::string mode)
{
    using namespace std;
    map<string, vector<Element *>> *map_ = mode == "tag" ? &element_tag_name_map : &element_class_name_map;
    auto iter = map_->find(key);
    if (iter == map_->end())
    {
        vector<Element *> new_vec;
        new_vec.push_back(temp);
        map_->insert(pair(key, new_vec));
    }
    else
    {
        iter->second.push_back(temp);
    }
}
void HtmlFile::openFile(const std::string &path)
{
    using namespace std;
    ifstream html_file(path, ios::in);
    string res;
    string temp;
    if (!html_file.is_open())
    {
        cout << "文件打开失败" << endl;
    }
    while (getline(html_file, temp))
    {
        res += temp;
    }
    mainParse(res);
}
void HtmlFile::mainParse(const std::string &ori_text)
{
    using namespace std;

    string ori_txt = ori_text + "</root>";
    stack<pair<Element *, string::const_iterator>> element_stack;
    stack<Element *> layer_stack;
    layer_stack.push(root_node);
    element_stack.push(pair(root_node, ori_txt.cbegin()));

    regex reg("<([^>]*)>");
    stack<pair<string, string::const_iterator>> parse_stack;
    auto words_begin = sregex_iterator(ori_txt.cbegin(), ori_txt.cend(), reg);
    auto words_end = sregex_iterator();

    bool is_last_finish = false;

    for (sregex_iterator k = words_begin; k != words_end; ++k)
    {
        smatch match = *k;
        string node_text = match.str(1);
        string node_name;
        if (node_text[0] == '/')
        {
            // 标签结束标识
            string new_text(node_text.cbegin() + 1, node_text.cend());
            node_name = Element::getNodeName(new_text);
            Element *stack_ele = element_stack.top().first;

            while (stack_ele->node_name_ != node_name)
            {
                stack_ele = element_stack.top().first;
                string node_value(element_stack.top().second, ori_txt.cbegin() + match.position());
                stack_ele->node_value_ = node_value;
                element_stack.pop();
            }
            element_stack.pop();
            if (layer_stack.top()->node_name_ == node_name)
            {
                layer_stack.pop();
            }
            is_last_finish = true;
        }
        else
        {
            // 标签添加标识
            string::const_iterator end_iter = ori_txt.cbegin() + match.position() + node_text.length() + 2;
            node_name = Element::getNodeName(node_text);
            Element *temp = new Element(node_text);

            if (!node_name.empty())
            {
                addClassTagMap(node_name, temp, "tag");
            }

            if (!temp->getAttribute("id").empty())
            {
                element_id_map.insert(pair(temp->getAttribute("id"), temp));
            }
            if (!temp->getAttribute("class").empty())
            {
                addClassTagMap(temp->getAttribute("class"), temp, "class");
            }

            if (is_last_finish)
            {
                temp->setParent(layer_stack.top());
                element_stack.push(pair(temp, end_iter));
            }
            else
            {
                auto last_pair = element_stack.top();
                Element *last_ele = last_pair.first;

                string last_node_name = last_ele->nodeName();
                regex reg("</" + last_node_name + ">");
                smatch no_use_res;
                auto ret = regex_search(end_iter, ori_txt.cend(), no_use_res, reg);
                if (ret)
                {
                    layer_stack.push(last_ele);
                    temp->setParent(last_ele);
                }
                else
                {
                    element_stack.pop();
                    string node_value(last_pair.second, ori_txt.cbegin() + match.position());
                    last_ele->node_value_ = node_value;
                    temp->setParent(layer_stack.top());
                }
                element_stack.push(pair(temp, end_iter));
            }
            is_last_finish = false;
        }
    }
}
Element *HtmlFile::getElementById(const std::string &id){
    auto iter = element_id_map.find(id);
    return iter != element_id_map.end() ? iter->second : nullptr;
}


int main()
{
    using namespace std;
    HtmlFile test = HtmlFile("page.html");
    cout << test.getElementById("pic_text") << endl; 

    return 0;
}
