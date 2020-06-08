def ex4(s):
    def is_digit(c):
        return '0' <= str(c) <= '9'

    def is_alpha(c):
        return 'a' <= str(c) <= 'z' or 'A' <= str(c) <= 'Z'

    s = '[' + s + ']'
    st = []
    for c in s:
        if is_digit(c):
            # Push number to stack, aggregate value if the element before it is also a number
            before_num = 0
            if len(st) and is_digit(st[-1]):
                before_num = st.pop()
            st.append(before_num * 10 + int(c))
        
        elif is_alpha(c):
            # Push string, aggregate value if the element before it is also string
            if len(st) and is_alpha(st[-1]):
                c = st.pop() + c
            st.append(c)

        elif c == '[':
            # Push [
            st.append(c)

        elif c == ']':
            # Process string
            s1 = ""
            while True:
                c1 = st.pop()
                if c1 == '[':
                    break
                s1 = c1 + s1

            # Get number to duplicate
            num = 1
            if len(st) and is_digit(st[-1]):
                num = st.pop()
            s1 = s1 * num 

            # Push back string to stack, aggregate value if the element before it is also string
            if len(st) and is_alpha(st[-1]):
                s1 = st.pop() + s1 
            st.append(s1)

    return st[0]
            