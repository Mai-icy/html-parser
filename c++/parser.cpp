#include "parser.h"

inline Element::Element(const std::string &tag_txt, const std::string &value) : parent_(nullptr), value_(value)
{
    parse_attribute(tag_txt);
}
void Element::parse_attribute(const std::string &tag_txt)
{
    using namespace std;
    tag_ = get_tag_type(tag_txt);
    regex words_regex("(\\S*)[\\s]*=[\\s]*['\"]([^>\\s]*)['\"]");
    auto words_begin = sregex_iterator(tag_txt.cbegin(), tag_txt.cend(), words_regex);
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
void Element::show()
{
    std::cout << "标签类型:" << tag_ << " 内容：" << value_ << std::endl;
}

void parse_ml(const std::string &ori_text)
{
    using namespace std;
    regex reg("<([^>]*)>");
    stack<pair<string, string::const_iterator>> parse_stack;

    auto words_begin = sregex_iterator(ori_text.cbegin(), ori_text.cend(), reg);
    auto words_end = sregex_iterator();
    cout << "开始" << endl;
    for (sregex_iterator k = words_begin; k != words_end; ++k)
    {
        smatch match = *k;
        string tag_text = match.str(1);

        string tag_type;
        if (tag_text[0] == '/')
        {
            string new_text(tag_text.cbegin() + 1, tag_text.cend());
            tag_type = get_tag_type(new_text);

            while (true)
            {
                auto top_pair = parse_stack.top();
                parse_stack.pop();
                string top_text = top_pair.first;
                string top_type = get_tag_type(top_text);
                if (top_type == tag_type)
                {
                    cout << "弹出" << top_type << endl;
                    string value(top_pair.second, ori_text.cbegin() + match.position());
                    Element ele(top_text, value);
                    break;
                }
                else
                {
                    Element ele(top_text, "");
                    cout << tag_text << endl;
                }
            }
        }
        else
        {
            string::const_iterator end_iter = ori_text.cbegin() + match.position() + tag_text.length() + 2;
            cout << "压入" << get_tag_type(tag_text) << endl;
            parse_stack.push(pair(tag_text, end_iter));
        }
    }
}

std::string get_tag_type(const std::string &tag_text)
{
    using namespace std;
    regex type_reg("([^=\\s]*)");
    smatch result;
    auto ret = regex_search(tag_text.cbegin(), tag_text.cend(), result, type_reg);
    return ret ? result.str(1) : "";
}

std::string read_html(const std::string &html_path)
{
    using namespace std;
    ifstream html_file(html_path, ios::in);
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
    return res;
}

int main()
{
    using namespace std;

    string test{"123<xml>value</xml>456<s></s>"};

    string content = read_html("page.html");
    parse_ml(content);

    return 0;
}