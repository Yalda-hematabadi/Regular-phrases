import re
import timeit

def expression_match(text: str):

    patterns = [("pattern_1",r"((ab)*(cd)*)*"), 
                ("pattern_2",r"(ab|cd)*"), 
                ("pattern_3",r"(aa)*b(aa)*|a(aa)*ba(aa)*"), 
                ("pattern_4",r"(a|ba)*(b|la)"), 
                ("pattern_5",r"(a*baa*)*(b|la)|a*(b|la)"), 
                ("pattern_6",r"(aa)*(ba|ab)(bb|(ba|ab)(aa)*(ba|ab))*")] 
    matches = []
    for pattern_name, pattern in patterns:
        if re.fullmatch(pattern, text):
            matches.append(pattern_name)

    if len(matches) == 0:
        print("the didn't match to any expression")
    else:
        print(f"matched expressions:{matches}")
        
    for pattern_name, pattern in patterns:
        setup_code = f"import re; pattern = re.compile({repr(pattern)})"
        stmt = f"pattern.fullmatch({repr(text)})"
        time_taken = timeit.timeit(stmt, setup=setup_code, number=100000)
        print(f"Time taken for {pattern_name}: {time_taken:.6f} seconds")
    
    
def main():
    text = input()
    expression_match(text)
    
if __name__ =='__main__':
    main()