import streamlit as st 
from text_extractor import extract_pdf,extract_txt
from ques_generator import ques_generator

def display_mcq(questions):
    for q in questions:
        st.markdown("### " + q['question'])
        choices = [q['answer']] + q['distractors']
        correct_answer = q['answer']
        
        user_answer = st.radio("Choose your answer:", choices)
        
        if st.button("Submit Answer"):
            if user_answer == correct_answer:
                st.success("Correct!")
            else:
                st.error("Wrong answer. The correct answer is: " + correct_answer)
        
        st.write("---")  




def main():
    st.title("Quiz Generator")
    st.markdown("Welcome! Let's create a personalised quiz for you. Please submit the context for which you want to create the quiz.")
  

    upld_file=st.file_uploader("Upload a .pdf or .txt file only.",accept_multiple_files=False,type=["pdf","txt"])
    typed_input=st.text_input("Enter your text within 1500 characters", value="", max_chars=1500, placeholder="Input over the character limit, will not be accepted.")
    num_ques_input=st.number_input("Number of questions to generate:", value=2)

    
    if st.button("Generate"):        
        if upld_file is not None and typed_input:
            st.warning('Please use only one option to submit content. (Use either the input box or upload a file option)', icon="⚠️")
        elif upld_file is not None:  
            if upld_file.type == "application/pdf":
                text = extract_pdf(upld_file)
            elif upld_file.type == "text/plain":
                st.write(upld_file.type)
                text = extract_txt(upld_file)
            else:
                st.error("Unsupported file type. Please upload a PDF or TXT file.")
                return
            st.success("File uploaded successfully.")
            st.write("Extracted Text:")
            st.write(text)
            
        elif typed_input != "": 
            st.success("Text input received successfully.")
            st.write("Typed Text:")
            st.write(typed_input)

            try:
                questions = ques_generator(typed_input,num_ques_input)
                display_mcq(questions)  
            except Exception as e:
                st.error(f"An error occurred: {e}")
            
        else:
            st.info("Please give an input.")
        


if __name__=="__main__":
    main()