# Custom string methods – completely manual, no built-in string methods used

#Convert to uppercase
def ye_upper(s):
    result = ""
    for ch in s:
        ascii_code = ord(ch)
        if 97 <= ascii_code <= 122:
            result += chr(ascii_code - 32)
        else:
            result += ch
    return result

#Convert to Lowercase
def ye_lower(s):
    result = ""
    for ch in s:
        ascii_code = ord(ch)
        if 65 <= ascii_code <= 90:
            result += chr(ascii_code + 32)
        else:
            result += ch
    return result

#First character upper, rest lower
def ye_capitalize(s):
    if not s:
        return s
    return ye_upper(s[0]) + ye_lower(s[1:])

#Swap case
def ye_swapcase(s):
    result = ""
    for ch in s:
        ascii_code = ord(ch)
        if 97 <= ascii_code <= 122:
            result += chr(ascii_code - 32)
        elif 65 <= ascii_code <= 90:
            result += chr(ascii_code + 32)
        else:
            result += ch
    return result

# Title case
def ye_title(s):
    result = ""
    capitalize_next = True
    for ch in s:
        if ch in " \t\n\r\f\v":
            result += ch
            capitalize_next = True
        else:
            if capitalize_next:
                result += ye_upper(ch)
            else:
                result += ye_lower(ch)
            capitalize_next = False
    return result

# Remove spaces or specified characters from start and end
def ye_strip(s ,chars = None):
    if chars is None:
        chars = "\t\n\r\f\v "
    start = 0
    while start < len(s) and s[start] in chars:
        start += 1
    end = len(s)
    while end > start and s[end - 1] in chars:
        end -= 1
    return s[start:end]

#Remove spaces or specified characters from Left
def ye_lstrip(s , chars = None):
    if chars is None:
        chars = "\t\n\r\f\v "
    start = 0
    while start < len(s) and s[start] in chars:
        start += 1
    return s[start:]

#Remove spaces or specified characters from Right
def ye_rstrip(s , chars = None):
    if chars is None:
        chars = "\t\n\r\f\v "
    end = len(s)
    while end > 0 and s[end - 1] in chars:
        end -= 1
    return s[:end]

#Center
def ye_center(s , width , fillchar = " "):
    if width <= len(s):
        return s
    left = (width - len(s))//2
    right = width - len(s) - left
    return fillchar * left + s + fillchar * right

# right just
def ye_rjust(s, width , fillchar = " "):
    if width <= len(s):
        return s
    return fillchar * (width - len(s)) + s 

#Left just
def ye_ljust(s, width , fillchar = " "):
    if width <= len(s):
        return s
    return s + fillchar * (width - len(s))

#Zero Fill
def ye_zfill(s , width):
    if len(s) >= width:
        return s

    if len(s) > 0 and s[0] == "-":
        return "-" + "0" * (width - len(s)) + s[1:]

    return "0" * (width - len(s)) + s

# Return index of first occurrence or -1
def ye_find(s , sub , start = 0):
    if not sub:
        return start
    for i in range(start, len(s) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i 
    return -1

# Count non-overlapping occurrences
def ye_count(s , sub):
    if not sub:
        return 0
    count = 0
    position = 0
    while True:
        position = ye_find(s , sub, position)
        if position == -1:
            break
        count +=1
        position += len(sub)
    return count

# Replace old substring with new one (optionally limited times)
def ye_replace(s , old , new , maxreplace = -1):
    if not old:
        return s
    result = ""
    position = 0
    replaced = 0
    while position < len(s):
        if s[position:position + len(old)] == old and (maxreplace == -1 or replaced < maxreplace):
            result += new
            position += len(old)
            replaced += 1
        else:
            result += s[position]
            position += 1
    return result

# Checks if the string s starts with the specified text and returns True or False
def ye_startswith(s , prefix):
    if len(prefix) > len(s):
        return False
    return s[:len(prefix)] == prefix

# Checks if the string s ends with the specified text and returns True or False
def ye_endswith(s , suffix):
    if len(suffix) > len(s):
        return False
    if not suffix:               # handle empty suffix
        return True
    return s[-len(suffix):] == suffix

# Returns True if all characters in the string are digits, otherwise False
def ye_isdigit(s):
    if not s :
        return False
    for ch in s:
        ascii_code = ord(ch)
        if not(48 <= ascii_code <= 57):
            return False
    return True

# Returns True if all characters in the string are letters, otherwise False
def ye_isalpha(s):
    if not s :
        return False
    for ch in s:
        ascii_code = ord(ch)
        if not(65 <= ascii_code <= 90 or 97 <= ascii_code <= 122):
            return False
    return True

# Returns True if all characters in the string are letters or digits, otherwise False
def ye_isalnum(s):
    if not s:
        return False
    for ch in s:
        ascii_code = ord(ch)
        if not(65 <= ascii_code <= 90 or 97 <= ascii_code <= 122 or 48 <= ascii_code <= 57):
            return False
    return True
    
# Returns True if all alphabetic characters in the string are lowercase, otherwise False
def ye_islower(s):
    has_cased = False
    for ch in s :
        ascii_code = ord(ch)
        if(65 <= ascii_code <=90):
            return False
        if(97 <= ascii_code <= 122):
            has_cased = True
    return has_cased

# Returns True if all alphabetic characters in the string are uppercase, otherwise False
def ye_isupper(s):
    has_cased = False
    for ch in s :
        ascii_code = ord(ch)
        if(97 <= ascii_code <= 122):
            return False
        if(65 <= ascii_code <=90):
            has_cased = True
    return has_cased

# Returns True if all characters in the string are whitespace characters, otherwise False
def ye_isspace(s):
    if not s:
        return False
    for ch in s:
        if ch not in "\t\n\r\f\v " :
            return False
    return True
 
# Returns a copy of the string with the specified prefix removed if it starts with it, otherwise returns the original string
def ye_removeprefix(s , prefix):
    if ye_startswith(s , prefix):
        return s[len(prefix):]
    return s

# Returns a copy of the string with the specified suffix removed if it ends with it, otherwise returns the original string
def ye_removesuffix(s , suffix):
    if ye_endswith(s , suffix):
        return s[:-len(suffix)]
    return s
    


#======================== MAIN Program :) ============================

print("Welcome to My Custom String Methods Program!")
print("You can use it to explore various string operations, just like Python's built-in methods.")

current = input("Enter the string :")

while True:
    print("\n" + "=" * 60)
    print("Current String --> " , repr(current))
    print("-" * 60)
    print("1.  upper     2.lower    3.capitalize    4. swapcase ")
    print("5.  title     6.strip    7.lstrip        8.rstrip ")
    print("9.  center   10.rjust   11.ljust        12.zfill ")
    print("13. find     14.count   15.replace      16.startswith")
    print("17. endswith    18.isdigit     19.isalpha")
    print("20. isalnum     21.islower     22.isupper")
    print("23. isspace     24.removeprefix")
    print("25. removesuffix")
    print("0.  Exit")
    print("=" * 60)

    choice = int(ye_strip(input("\n Choose a number (0 to Exit) : ")))


    if choice == 0:
        print("Good Bye! :)...")
        break


    result = current
    try:
        n = choice
        if n == 1:
            result = ye_upper(current)

        elif n == 2:
            result = ye_lower(current)

        elif n == 3:
            result = ye_capitalize(current)

        elif n == 4:
            result = ye_swapcase(current)

        elif n == 5:
            result = ye_title(current)

        elif n == 6:
            chars = input("Characters to strip (Enter = Whitespace) :") or None
            result = ye_strip(current , chars)

        elif n == 7:
            chars = input("Characters to strip (Enter = Whitespace) :") or None
            result = ye_lstrip(current , chars)

        elif n == 8:
            chars = input("Characters to strip (Enter = Whitespace) :") or None
            result = ye_rstrip(current , chars)

        elif n == 9:
            width = int(input("Width: "))
            fill = input("Fill character (Enter = space) : ") or " "
            result = ye_center(current , width , fill)

        elif n == 10:
            width = int(input("Width: "))
            fill = input("Fill character (Enter = space) : ") or " "
            result = ye_rjust(current , width , fill)

        elif n == 11:
            width = int(input("Width: "))
            fill = input("Fill character (Enter = space) : ") or " "
            result = ye_ljust(current , width , fill)

        elif n == 12:
            width = int(input("Width: "))
            result = ye_zfill(current , width)

        elif n == 13:
            sub = input("Substring to find : ")
            result = ye_find(current , sub)
            print("First position -->" , result)
            result = current

        elif n == 14:
            sub = input("Substring to count : ")
            result = ye_count(current , sub)
            print("Count -->" , result)
            result = current

        elif n == 15:
            old = input("Old substring: ")
            new = input("New substring: ")
            cnt = input("Max replacements (-1 = all, Enter = all): ")
            cnt = -1 if not cnt or cnt == "-1" else int(cnt)
            result = ye_replace(current, old, new, cnt)

        elif n == 16:
            prefix = input("Prefix to check: ")
            print("startswith -->", ye_startswith(current, prefix))
            result = current

        elif n == 17:
            suffix = input("Suffix to check: ")
            print("endswith -->", ye_endswith(current, suffix))
            result = current

        elif n == 18:
            print("isdigit -->", ye_isdigit(current))
            result = current

        elif n == 19:
            print("isalpha --> ", ye_isalpha(current))
            result = current

        elif n == 20:
            print("isalnum --> ", ye_isalnum(current))
            result = current

        elif n == 21:
            print("islower --> ", ye_islower(current))
            result = current

        elif n == 22:
            print("isupper --> ", ye_isupper(current))
            result = current

        elif n == 23:
            print("isspace --> ", ye_isspace(current))
            result = current

        elif n == 24:
            prefix = input("Prefix to remove: ")
            result = ye_removeprefix(current, prefix)

        elif n == 25 :
            suffix = input("Suffix to remove: ")
            result = ye_removesuffix(current, suffix)

        else:
            print("Invalid choice !!!")
            continue

        # Only show result and ask to update when the operation returns a new string
        if n not in [13, 14, 16, 17, 18, 19, 20, 21, 22, 23]:
            print("Result --> " , repr(result))

        if n <= 25 and n not in [13, 14, 16, 17, 18, 19, 20, 21, 22, 23]:
            update = ye_upper(input("Update current string with this result? (y/n)"))
            if ye_lower(update) == "y":
                current = result



    except Exception as e:
        print("Error : " , e)