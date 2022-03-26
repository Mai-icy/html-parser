#include <iostream>
#include <regex>
#include <string>
#include <map>
#include <vector>
#include <stack>

int search_element(const std::string &text)
{
    using namespace std;
    regex reg("<(.*)>(.*)</(\\1)>");
    smatch result;
    auto ret = regex_search(text.cbegin(), text.cend(), result, reg);

    if (ret)
    {
        std::cout << "prefix:" << result.prefix() << std::endl;
        std::cout << "suffix:" << result.suffix() << std::endl;
        std::cout << "position:" << result.position()+ result.str(0).length() << std::endl;
        string tag(result.str(1));
        string value(result.str(2));

        cout << tag << "之后" << value << endl;
    }
    return 0;
}

std::string::const_iterator search_element2(const std::string &text, std::string &tag, std::string &value)
{
    using namespace std;
    regex reg("<([^>]*)>");
    smatch result;
    auto ret = regex_search(text.cbegin(), text.cend(), result, reg);

    if (ret)
    {
        std::cout << "prefix:" << result.prefix() << std::endl;
        std::cout << "suffix:" << result.suffix() << std::endl;
        std::cout << "position:" << result.position()+ result.str(0).length() << std::endl;
        tag = result.str(1);

        cout << tag << endl;
    }
    return text.cbegin();
}

int search_element3(const std::string &text)
{
    using namespace std;
    regex words_regex("(\\S*)[\\s]*=[\\s]*['\"]([^>\\s]*)['\"]");
    auto words_begin = sregex_iterator(text.cbegin(), text.cend(), words_regex);
    auto words_end = sregex_iterator();
    for (sregex_iterator k = words_begin; k != words_end; ++k) { 
        smatch match = *k; 
        string attr = match.str(1);
        string value = match.str(2);
        cout << attr << ":的值:" << value << endl;
    }
}




int main()
{
    using namespace std;

    string test{"a href='img/2.gi' id='nihao'"};
    search_element3(test);

    return 0;
}