mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
echo "web: sh setup.sh && streamlit run main.py" > Procfile