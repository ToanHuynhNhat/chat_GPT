import streamlit as st
import openai

openai.api_key = "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"





provscons = "You give cons and pros for any ideal"
swot = "You give SWOT for an ideal"
options =" compare the following options based on certain criteria and make the best choice."
causal_chain      = "causal chain of events will occur"


def chat(system,user):
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      temperature = 0.2,
      max_tokens = 500,
      messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": user}
      ]
    )
    return response['choices'][0]['message']['content']


def display_pros_vs_cons(input_text):
    st.write("Bạn đã chọn 'Pros vs Cons'.")
    st.write("Input của bạn là:", input_text)
    result = chat(provscons,input_text)
    st.write(f"Kết quả: \n {result}")

def display_swot(input_text):
    st.write("Bạn đã chọn 'SWOT'.")
    st.write("Input của bạn là:", input_text)
    # Logic cho 'SWOT' ở đây
    result = chat(swot,input_text)
    st.write(f"Kết quả: \n {result}")

def display_multi_option(input_text):
    st.write("Bạn đã chọn 'Multi-option'.")
    st.write("Input của bạn là:", input_text)
    result = chat(options,input_text)
    st.write(f"Kết quả: \n {result}")

def display_causal_chain(input_text):
    st.write("Bạn đã chọn 'Causal Chain'.")
    st.write("Input của bạn là:", input_text)
    result = chat(causal_chain,input_text)
    st.write(f"Kết quả: \n {result}")

# Tạo layout
st.title("Lựa chọn phân tích")
option = st.selectbox("Chọn một phương pháp phân tích:", ("Pros vs Cons", "SWOT", "Multi-option", "Causal Chain"))
input_text = st.text_input("Nhập input của bạn:")

# Xử lý lựa chọn
if option == "Pros vs Cons":
    display_pros_vs_cons(input_text)
elif option == "SWOT":
    display_swot(input_text)
elif option == "Multi-option":
    display_multi_option(input_text)
elif option == "Causal Chain":
    display_causal_chain(input_text)