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
    "def query_kb(query):\n",
    "    kb = {\n",
    "        \"dashboard\": \"You can access your dashboard at https://bookleaf.example.com/dashboard\",\n",
    "        \"author copy\": \"Author copies are shipped within 15 days of book live date\",\n",
    "        \"sales report\": \"Book sales reports are available monthly on your dashboard\",\n",
    "        \"add-on\": \"Add-ons include PR, Awards, and Bestseller packages. Contact support for details.\"\n",
    "    }\n",
    "    q_lower = query.lower()\n",
    "    for k, v in kb.items():\n",
    "        if k in q_lower:\n",
    "            return v\n",
    "    return \"I could not find a matching answer. A human agent will assist.\"\n"
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
