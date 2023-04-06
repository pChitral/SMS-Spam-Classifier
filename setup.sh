mkdir -p /app/.streamlit
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > /app/.streamlit/config.toml
