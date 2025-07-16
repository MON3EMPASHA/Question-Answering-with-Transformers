import streamlit as st
from transformers import pipeline
from evaluate import load
import time
from sample_data import sample_english, sample_arabic

# Set page config
st.set_page_config(
    page_title="Question Answering with Transformers",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Force light theme with CSS
st.markdown("""
<style>
    .stApp {
        background-color: white !important;
    }
    .main .block-container {
        background-color: white !important;
    }
    .css-1d391kg {
        background-color: white !important;
    }
    .css-1v0mbdj {
        background-color: #f0f2f6 !important;
    }
    .css-1lcbmhc {
        background-color: white !important;
    }
    .css-1v0mbdj.ebxwdo6 {
        background-color: #f0f2f6 !important;
    }
    .stMarkdown {
        color: #262730 !important;
    }
    .stText {
        color: #262730 !important;
    }
    .stSelectbox {
        color: #262730 !important;
    }
    .stRadio {
        color: #262730 !important;
    }
    .stTextArea {
        color: #262730 !important;
    }
</style>
""", unsafe_allow_html=True)

# Define model configurations (not loaded at startup)
qa_model_configs = {
    "English": {
        "BERT": "bert-large-uncased-whole-word-masking-finetuned-squad",
        "DistilBERT": "distilbert-base-cased-distilled-squad",
        "RoBERTa": "deepset/roberta-base-squad2",
        "DeBERTa": "timpal0l/mdeberta-v3-base-squad2",
    },
    "Arabic": {
        "BERT": "mrm8488/bert-multi-cased-finetuned-xquadv1",
        "XQuAD BERT (Arabic)": "mrm8488/bert-multi-cased-finetuned-xquadv1",
        "MultiBERT (Arabic)": "mrm8488/bert-multi-cased-finetuned-xquadv1"
    }
}

# Cache for loaded models
@st.cache_resource
def load_qa_model(model_name, model_path):
    """Load a QA model and cache it"""
    try:
        with st.spinner(f"Loading {model_name} model..."):
            return pipeline("question-answering", model=model_path)
    except Exception as e:
        st.error(f"Error loading {model_name}: {str(e)}")
        return None

st.title("Question Answering with Transformers")

# Sidebar: Language selection
lang = st.sidebar.selectbox("Select Language", ["English", "Arabic"])

# Sidebar: Model selection
model_options = list(qa_model_configs[lang].keys())
selected_models = st.sidebar.multiselect("Select Models", model_options, default=model_options[:1])

# Context input method - Try Sample Data is now first
context_mode = st.radio("Choose context input method:", ["Try Sample Data", "Manual Input"])

def get_answers_from_models(context, questions, selected_models, lang):
    """Get answers from selected models"""
    results = {}
    
    for model_name in selected_models:
        model_path = qa_model_configs[lang][model_name]
        qa_pipeline = load_qa_model(model_name, model_path)
        
        if qa_pipeline is None:
            continue
            
        model_results = []
        for question in questions:
            try:
                with st.spinner(f"Getting answer from {model_name}..."):
                    result = qa_pipeline({"context": context, "question": question})
                    if isinstance(result, dict) and 'answer' in result:
                        model_results.append(result['answer'])
                    else:
                        model_results.append("Unexpected result format")
            except Exception as e:
                st.error(f"Error getting answer from {model_name}: {str(e)}")
                model_results.append("Error occurred")
        
        results[model_name] = model_results
    
    return results

if context_mode == "Try Sample Data":
    # Sample data
    samples = sample_english if lang == "English" else sample_arabic
    sample_contexts = {f"Sample {i+1}": s for i, s in enumerate(samples)}
    sample_choice = st.selectbox("Choose a sample context:", list(sample_contexts.keys()))
    sample_obj = sample_contexts[sample_choice]
    context = sample_obj["context"]
    st.markdown(f"**Sample Context:**\n{context}")
    
    recommended_questions = sample_obj.get("recommended_questions", [sample_obj["question"]])
    reference_answers = sample_obj.get("answers", [])
    st.markdown("**Recommended Questions:**")
    for idx, q in enumerate(recommended_questions):
        st.write(f"- {q}")
    
    manual_q = st.text_area("Enter your own questions (one per line), or leave blank to use recommended:")
    if manual_q.strip():
        question_list = [q.strip() for q in manual_q.split("\n") if q.strip()]
        show_reference = False
    else:
        question_list = recommended_questions
        show_reference = True
    
    if st.button("Get Answers") and context and question_list and selected_models:
        results = get_answers_from_models(context, question_list, selected_models, lang)
        
        for i, question in enumerate(question_list):
            st.markdown(f"**Question {i+1}:** {question}")
            if show_reference and i < len(reference_answers):
                st.write(f"**Reference Answer:** {reference_answers[i]['text']}")
            for model_name, model_answers in results.items():
                if i < len(model_answers):
                    st.write(f"**{model_name}:** {model_answers[i]}")
            st.markdown("---")
else:
    # Manual input
    context = st.text_area(f"Enter your context in {lang}:")
    questions = st.text_area("Enter your questions (one per line):")
    question_list = [q.strip() for q in questions.split("\n") if q.strip()]
    
    if st.button("Get Answers") and context and question_list and selected_models:
        results = get_answers_from_models(context, question_list, selected_models, lang)
        
        for i, question in enumerate(question_list):
            st.markdown(f"**Question {i+1}:** {question}")
            for model_name, model_answers in results.items():
                if i < len(model_answers):
                    st.write(f"**{model_name}:** {model_answers[i]}")
            st.markdown("---")

# Sidebar links
st.sidebar.markdown("---")
st.sidebar.markdown("**Links:**")
st.sidebar.markdown("📊 [Kaggle Notebook](https://www.kaggle.com/code/abdelmonemhatem/question-answering-with-transformers)")
st.sidebar.markdown("👨‍💻 [Portfolio](https://abdelmonem-hatem.netlify.app/)") 