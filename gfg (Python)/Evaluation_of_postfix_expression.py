

class Solution:
    def evaluate(self, arr):
        # code here
        st = []
    
        for token in arr:
            if token in {"+", "-", "*", "/"}:  # If operator
                ele1 = st.pop()
                ele2 = st.pop()
    
                if token == "+":
                    st.append(ele2 + ele1)
                elif token == "-":
                    st.append(ele2 - ele1)  # Ensure correct order
                elif token == "*":
                    st.append(ele2 * ele1)
                elif token == "/":
                    # Match C++ division behavior (truncate towards zero)
                    st.append(int(ele2 / ele1))
            else:
                st.append(int(token))  # Convert number from string to integer
        
        return st[-1]