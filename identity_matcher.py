{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cdaf9581-a358-4e65-92d1-c55ed5ba7fb5",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'db'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdb\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;241m*\u001b[39m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mllm_engine\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m classify_query\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mrag_engine\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m query_kb\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'db'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "from openai import OpenAI\n",
    "\n",
    "# Ensure OpenAI key exists\n",
    "if \"OPENAI_API_KEY\" not in st.secrets:\n",
    "    st.error(\"OPENAI_API_KEY not found in Streamlit secrets\")\n",
    "    st.stop()\n",
    "\n",
    "client = OpenAI(api_key=st.secrets[\"OPENAI_API_KEY\"])\n",
    "\n",
    "SYSTEM_PROMPT = \"\"\"\n",
    "You are a publishing support AI.\n",
    "Classify user query into:\n",
    "book_live_status\n",
    "royalty_status\n",
    "author_copy\n",
    "dashboard_access\n",
    "add_on_status\n",
    "book_sales\n",
    "general_policy\n",
    "Return intent, confidence (0-100), requires_db (True/False)\n",
    "\"\"\"\n",
    "\n",
    "def classify_query(query):\n",
    "    try:\n",
    "        resp = client.chat.completions.create(\n",
    "            model=\"gpt-4o-mini\",\n",
    "            messages=[\n",
    "                {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n",
    "                {\"role\": \"user\", \"content\": query}\n",
    "            ],\n",
    "            temperature=0\n",
    "        )\n",
    "        # returns a dict\n",
    "        return eval(resp.choices[0].message.content)\n",
    "    except Exception as e:\n",
    "        # fallback simple rules\n",
    "        q = query.lower()\n",
    "        if \"live\" in q:\n",
    "            return {\"intent\": \"book_live_status\", \"confidence\": 90, \"requires_db\": True}\n",
    "        elif \"royalty\" in q:\n",
    "            return {\"intent\": \"royalty_status\", \"confidence\": 90, \"requires_db\": True}\n",
    "        else:\n",
    "            return {\"intent\": \"general_policy\", \"confidence\": 75, \"requires_db\": False}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1ce75b5-3ef3-4fef-99ed-987a6a9279ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
