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
    "import sqlite3\n",
    "import os\n",
    "\n",
    "DB_FILE = \"bookleaf.db\"\n",
    "\n",
    "def init_db():\n",
    "    if not os.path.exists(DB_FILE):\n",
    "        conn = sqlite3.connect(DB_FILE)\n",
    "        c = conn.cursor()\n",
    "        c.execute('''\n",
    "            CREATE TABLE books (\n",
    "                id INTEGER PRIMARY KEY,\n",
    "                author_email TEXT,\n",
    "                author_name TEXT,\n",
    "                book_title TEXT,\n",
    "                final_submission_date TEXT,\n",
    "                book_live_date TEXT,\n",
    "                royalty_status TEXT,\n",
    "                ISBN TEXT,\n",
    "                add_on_services TEXT\n",
    "            )\n",
    "        ''')\n",
    "        conn.commit()\n",
    "        conn.close()\n",
    "\n",
    "def seed_data():\n",
    "    conn = sqlite3.connect(DB_FILE)\n",
    "    c = conn.cursor()\n",
    "    # Add some mock books\n",
    "    c.execute(\"DELETE FROM books\")  # Reset table\n",
    "    c.execute('''\n",
    "        INSERT INTO books (author_email, author_name, book_title, final_submission_date, book_live_date, royalty_status, ISBN, add_on_services)\n",
    "        VALUES\n",
    "        ('sara.johnson@xyz.com','Sara J','Poetry Book','2023-09-01','2023-10-01','Paid','1234567890','PR Package'),\n",
    "        ('john.doe@xyz.com','John Doe','Fiction Novel','2023-08-15','2023-09-20','Pending','0987654321','Bestseller Package')\n",
    "    ''')\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "def get_book_by_author(email):\n",
    "    conn = sqlite3.connect(DB_FILE)\n",
    "    c = conn.cursor()\n",
    "    c.execute(\"SELECT * FROM books WHERE author_email=?\", (email,))\n",
    "    results = c.fetchall()\n",
    "    conn.close()\n",
    "    return results\n",
    "\n",
    "def log_query(user_email, query, intent, confidence, response, escalated, error_message=None):\n",
    "    conn = sqlite3.connect(DB_FILE)\n",
    "    c = conn.cursor()\n",
    "    c.execute('''\n",
    "        CREATE TABLE IF NOT EXISTS query_logs (\n",
    "            id INTEGER PRIMARY KEY,\n",
    "            user_email TEXT,\n",
    "            query TEXT,\n",
    "            intent TEXT,\n",
    "            confidence INTEGER,\n",
    "            response TEXT,\n",
    "            escalated INTEGER,\n",
    "            error_message TEXT\n",
    "        )\n",
    "    ''')\n",
    "    c.execute('''\n",
    "        INSERT INTO query_logs (user_email, query, intent, confidence, response, escalated, error_message)\n",
    "        VALUES (?, ?, ?, ?, ?, ?, ?)\n",
    "    ''', (user_email, query, intent, confidence, response, escalated, error_message))\n",
    "    conn.commit()\n",
    "    conn.close()\n"
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
