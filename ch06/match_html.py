# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from ch06.array_stack import ArrayStack


def is_matched_html(raw):
    """Return True if all HTML tags are properly match; False otherwise."""
    S = ArrayStack()
    j = raw.find('<')  # find first '<' character (if any)
    while j != -1:
        k = raw.find('>', j + 1)  # find next '>' character
        if k == -1:
            return False  # invalid tag
        tag = raw[j + 1:k]  # strip away < >
        if not tag.startswith('/'):  # this is opening tag
            S.push(tag)
        else:  # this is closing tag
            if S.is_empty():
                return False  # nothing to match with
            if tag[1:] != S.pop():
                return False  # mismatched delimiter
        j = raw.find('<', k + 1)  # find next '<' character (if any)
    return S.is_empty()  # were all opening tags matched?


if __name__ == '__main__':
    html = """
    <body>
        <center>
            <h1> The Little Boat </h1>
        </center>
        <p> The storm tossed the little
        boat like a cheap sneaker in an
        old washing machine. The three
        drunken fishermen were used to
        such treatment, of course, but
        not the tree salesman, who even as
        a stowaway now felt that he
        had overpaid for the voyage. </p>  
        <ol>
            <li> Will the salesman die? </li>
            <li> What color is the boat? </li>
            <li> And what about Naomi? </li>
        </ol>
    </body>
    """
    print(is_matched_html(html))
