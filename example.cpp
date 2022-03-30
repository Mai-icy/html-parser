#include "html_parser.hpp"


int main()
{
    using namespace std;
    HtmlFile test = HtmlFile("example.html");
    cout << *(test.getElementById("pic_text")) << endl;
    cout << *(test.getElementById("placeholder")) << endl;
    return 0;
}
