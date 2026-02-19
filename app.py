{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cdaf9581-a358-4e65-92d1-c55ed5ba7fb5",
   "metadata": {},
   "outputs": [
    {
     "ename": "OpenAIError",
     "evalue": "The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOpenAIError\u001b[0m                               Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 4\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mjson\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mopenai\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m OpenAI\n\u001b[1;32m----> 4\u001b[0m client \u001b[38;5;241m=\u001b[39m OpenAI()\n\u001b[0;32m      6\u001b[0m SYSTEM_PROMPT \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;124mYou are a publishing support AI.\u001b[39m\n\u001b[0;32m      8\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[38;5;124m}\u001b[39m\n\u001b[0;32m     26\u001b[0m \u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[0;32m     29\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mclassify_query\u001b[39m(query):\n",
      "File \u001b[1;32mE:\\anaconda\\Lib\\site-packages\\openai\\_client.py:116\u001b[0m, in \u001b[0;36mOpenAI.__init__\u001b[1;34m(self, api_key, organization, project, base_url, websocket_base_url, timeout, max_retries, default_headers, default_query, http_client, _strict_response_validation)\u001b[0m\n\u001b[0;32m    114\u001b[0m     api_key \u001b[38;5;241m=\u001b[39m os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mOPENAI_API_KEY\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    115\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m api_key \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 116\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m OpenAIError(\n\u001b[0;32m    117\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    118\u001b[0m     )\n\u001b[0;32m    119\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mapi_key \u001b[38;5;241m=\u001b[39m api_key\n\u001b[0;32m    121\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m organization \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "\u001b[1;31mOpenAIError\u001b[0m: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import os\n",
    "client = OpenAI(api_key=os.getenv(\"OPENAI_API_KEY\"))\n",
    "\n",
    "SYSTEM_PROMPT = \"\"\"\n",
    "You are a publishing support AI.\n",
    "\n",
    "Classify user query into:\n",
    "\n",
    "book_live_status\n",
    "royalty_status\n",
    "author_copy\n",
    "dashboard_access\n",
    "add_on_status\n",
    "book_sales\n",
    "general_policy\n",
    "\n",
    "Return ONLY JSON:\n",
    "{\n",
    " \"intent\":\"...\",\n",
    " \"confidence\":0-100,\n",
    " \"requires_db\":true/false\n",
    "}\n",
    "\"\"\"\n",
    "\n",
    "\n",
    "def classify_query(query):\n",
    "    resp = client.chat.completions.create(\n",
    "        model=\"gpt-4o-mini\",\n",
    "        messages=[\n",
    "            {\"role\": \"system\", \"content\": SYSTEM_PROMPT},\n",
    "            {\"role\": \"user\", \"content\": query}\n",
    "        ],\n",
    "        temperature=0\n",
    "    )\n",
    "\n",
    "    return json.loads(resp.choices[0].message.content)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
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
