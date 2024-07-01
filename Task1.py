import re

def chatbot_response(user_input):
    # Convert user input to lower case to make the bot case insensitive
    user_input = user_input.lower()

    # Define responses
    if re.search(r'\b(who is the captain of the indian cricket team)\b', user_input):
        return "As of the latest update, Rohit Sharma is the captain of the Indian cricket team."
    elif re.search(r'\b(who is the highest run scorer in odi cricket)\b', user_input):
        return "Sachin Tendulkar is the highest run scorer in ODI cricket."
    elif re.search(r'\b(who has the most wickets in test cricket)\b', user_input):
        return "Muttiah Muralitharan has the most wickets in Test cricket."
    elif re.search(r'\b(who won the first cricket world cup)\b', user_input):
        return "The West Indies won the first Cricket World Cup in 1975."
    elif re.search(r'\b(what is the highest individual score in test cricket)\b', user_input):
        return "Brian Lara holds the highest individual score in Test cricket with 400 not out."
    elif re.search(r'\b(who has the most centuries in international cricket)\b', user_input):
        return "Sachin Tendulkar has the most centuries in international cricket."
    elif re.search(r'\b(what is the nickname of the australian cricket team)\b', user_input):
        return "The Australian cricket team is nicknamed the 'Baggy Greens'."
    elif re.search(r'\b(who is known as the king of swing)\b', user_input):
        return "Wasim Akram is known as the 'King of Swing'."
    elif re.search(r'\b(who is the fastest bowler in cricket history)\b', user_input):
        return "Shoaib Akhtar is considered the fastest bowler in cricket history."
    elif re.search(r'\b(what is the largest cricket stadium in the world)\b', user_input):
        return "The Narendra Modi Stadium in Ahmedabad, India is the largest cricket stadium in the world."
    elif re.search(r'\b(who is the first batsman to score a double century in odi)\b', user_input):
        return "Sachin Tendulkar was the first batsman to score a double century in ODI cricket."
    elif re.search(r'\b(what is the highest team total in test cricket)\b', user_input):
        return "Sri Lanka holds the record for the highest team total in Test cricket with 952/6 declared."
    elif re.search(r'\b(who has the most sixes in international cricket)\b', user_input):
        return "Chris Gayle holds the record for the most sixes in international cricket."
    elif re.search(r'\b(what is the length of a cricket pitch)\b', user_input):
        return "The length of a cricket pitch is 22 yards (20.12 meters)."
    elif re.search(r'\b(who won the icc world cup 2019)\b', user_input):
        return "England won the ICC World Cup 2019."
    elif re.search(r'\b(who has the most catches in test cricket)\b', user_input):
        return "Rahul Dravid has the most catches in Test cricket."
    elif re.search(r'\b(what is the highest individual score in odi cricket)\b', user_input):
        return "Rohit Sharma holds the highest individual score in ODI cricket with 264 runs."
    elif re.search(r'\b(who is the fastest to 10,000 runs in odi cricket)\b', user_input):
        return "Virat Kohli is the fastest to 10,000 runs in ODI cricket."
    elif re.search(r'\b(who is the fastest to 400 wickets in test cricket)\b', user_input):
        return "Ravichandran Ashwin is the fastest to 400 wickets in Test cricket."
    elif re.search(r'\b(who has the best bowling figures in odi cricket)\b', user_input):
        return "Chaminda Vaas holds the best bowling figures in ODI cricket with 8/19."
    elif re.search(r'\b(who has the most five-wicket hauls in test cricket)\b', user_input):
        return "Muttiah Muralitharan has the most five-wicket hauls in Test cricket."
    elif re.search(r'\b(what is the fastest century in odi cricket)\b', user_input):
        return "AB de Villiers holds the record for the fastest century in ODI cricket, scored in 31 balls."
    elif re.search(r'\b(who has the most stumpings in international cricket)\b', user_input):
        return "MS Dhoni holds the record for the most stumpings in international cricket."
    elif re.search(r'\b(who has the most double centuries in test cricket)\b', user_input):
        return "Don Bradman has the most double centuries in Test cricket with 12."
    elif re.search(r'\b(what is the highest partnership in odi cricket)\b', user_input):
        return "Chris Gayle and Marlon Samuels hold the highest partnership in ODI cricket with 372 runs."
    elif re.search(r'\b(who is the youngest player to score a century in test cricket)\b', user_input):
        return "Mohammad Ashraful is the youngest player to score a century in Test cricket."
    elif re.search(r'\b(what is the highest individual score in t20 cricket)\b', user_input):
        return "Chris Gayle holds the highest individual score in T20 cricket with 175 not out."
    elif re.search(r'\b(who is the first player to score 10,000 runs in test cricket)\b', user_input):
        return "Sunil Gavaskar was the first player to score 10,000 runs in Test cricket."
    elif re.search(r'\b(who has the most hat-tricks in odi cricket)\b', user_input):
        return "Lasith Malinga holds the record for the most hat-tricks in ODI cricket."
    elif re.search(r'\b(who has the most runs in a single odi world cup)\b', user_input):
        return "Sachin Tendulkar scored the most runs in a single ODI World Cup with 673 runs in 2003."
    elif re.search(r'\b(what is the longest cricket match)\b', user_input):
        return "The longest cricket match was played between England and South Africa in 1939, lasting for 12 days."
    elif re.search(r'\b(who has the most wickets in a single odi world cup)\b', user_input):
        return "Glenn McGrath has the most wickets in a single ODI World Cup with 26 wickets in 2007."
    elif re.search(r'\b(who has the highest batting average in test cricket)\b', user_input):
        return "Don Bradman has the highest batting average in Test cricket with 99.94."
    elif re.search(r'\b(who is the first player to take 10 wickets in an innings)\b', user_input):
        return "Jim Laker was the first player to take 10 wickets in an innings."
    elif re.search(r'\b(who has the most runs in test cricket)\b', user_input):
        return "Sachin Tendulkar has the most runs in Test cricket."
    elif re.search(r'\b(what is the highest successful run chase in test cricket)\b', user_input):
        return "The highest successful run chase in Test cricket is 418 by the West Indies against Australia in 2003."
    elif re.search(r'\b(who has the most sixes in test cricket)\b', user_input):
        return "Brendon McCullum holds the record for the most sixes in Test cricket."
    elif re.search(r'\b(what is the lowest team total in test cricket)\b', user_input):
        return "The lowest team total in Test cricket is 26 by New Zealand against England in 1955."
    elif re.search(r'\b(who has the most not outs in test cricket)\b', user_input):
        return "James Anderson has the most not outs in Test cricket."
    elif re.search(r'\b(who has the most ducks in odi cricket)\b', user_input):
        return "Sanath Jayasuriya holds the record for the most ducks in ODI cricket."
    elif re.search(r'\b(who is the first player to score a century in t20 cricket)\b', user_input):
        return "Chris Gayle was the first player to score a century in T20 cricket."
    elif re.search(r'\b(who has the most five-wicket hauls in odi cricket)\b', user_input):
        return "Waqar Younis has the most five-wicket hauls in ODI cricket."
    elif re.search(r'\b(what is the highest team total in odi cricket)\b', user_input):
        return "England holds the record for the highest team total in ODI cricket with 481/6."
    elif re.search(r'\b(who has the most catches in odi cricket)\b', user_input):
        return "Mahela Jayawardene has the most catches in ODI cricket."
    elif re.search(r'\b(who has the most runs in t20 cricket)\b', user_input):
        return "Virat Kohli has the most runs in T20 international cricket."
    elif re.search(r'\b(what is the highest team total in t20 cricket)\b', user_input):
        return "Afghanistan holds the record for the highest team total in T20 international cricket with 278/3."
    elif re.search(r'\b(who has the most wickets in t20 cricket)\b', user_input):
        return "Shakib Al Hasan has the most wickets in T20 international cricket."
    elif re.search(r'\b(what is the fastest fifty in odi cricket)\b', user_input):
        return "AB de Villiers holds the record for the fastest fifty in ODI cricket, scored in 16 balls."
    elif re.search(r'\b(who has the most runs in a calendar year in odi cricket)\b', user_input):
        return "Sachin Tendulkar scored the most runs in a calendar year in ODI cricket with 1,894 runs in 1998."
    elif re.search(r'\b(what is the fastest century in test cricket)\b', user_input):
        return "Brendon McCullum holds the record for the fastest century in Test cricket, scored in 54 balls."
    elif re.search(r'\b(who has the most runs in a single t20 world cup)\b', user_input):
        return "Virat Kohli scored the most runs in a single T20 World Cup with 319 runs in 2014."
    elif re.search(r'\b(who has the most wickets in a single t20 world cup)\b', user_input):
        return "Ajantha Mendis holds the record for the most wickets in a single T20 World Cup with 15 wickets in 2012."
    elif re.search(r'\b(what is the fastest fifty in t20 cricket)\b', user_input):
        return "Yuvraj Singh holds the record for the fastest fifty in T20 international cricket, scored in 12 balls."
    elif re.search(r'\b(who has the most matches as captain in international cricket)\b', user_input):
        return "MS Dhoni has captained the most matches in international cricket."
    elif re.search(r'\b(who has the most stumpings in test cricket)\b', user_input):
        return "Bert Oldfield holds the record for the most stumpings in Test cricket."
    elif re.search(r'\b(what is the highest individual score in women\'s odi cricket)\b', user_input):
        return "Belinda Clark holds the highest individual score in women's ODI cricket with 229 not out."
    elif re.search(r'\b(who has the most runs in women\'s test cricket)\b', user_input):
        return "Jan Brittin has the most runs in women's Test cricket."
    elif re.search(r'\b(what is the highest team total in women\'s t20 cricket)\b', user_input):
        return "South Africa holds the highest team total in women's T20 international cricket with 205/1."
    elif re.search(r'\b(who has the most wickets in women\'s odi cricket)\b', user_input):
        return "Jhulan Goswami has the most wickets in women's ODI cricket."
    elif re.search(r'\b(what is the fastest century in women\'s t20 cricket)\b', user_input):
        return "Deandra Dottin holds the record for the fastest century in women's T20 international cricket, scored in 38 balls."
    elif re.search(r'\b(who has the most sixes in women\'s t20 cricket)\b', user_input):
        return "Sophie Devine holds the record for the most sixes in women's T20 international cricket."
    elif re.search(r'\b(who has the most runs in women\'s t20 cricket)\b', user_input):
        return "Suzie Bates has the most runs in women's T20 international cricket."
    elif re.search(r'\b(who has the most five-wicket hauls in women\'s odi cricket)\b', user_input):
        return "Cathryn Fitzpatrick holds the record for the most five-wicket hauls in women's ODI cricket."
    elif re.search(r'\b(what is the highest individual score in women\'s test cricket)\b', user_input):
        return "Kiran Baluch holds the highest individual score in women's Test cricket with 242."
    elif re.search(r'\b(who has the most centuries in women\'s odi cricket)\b', user_input):
        return "Mithali Raj holds the record for the most centuries in women's ODI cricket."
    elif re.search(r'\b(who has the most wickets in women\'s t20 cricket)\b', user_input):
        return "Anisa Mohammed has the most wickets in women's T20 international cricket."
    elif re.search(r'\b(what is the highest team total in women\'s odi cricket)\b', user_input):
        return "New Zealand holds the highest team total in women's ODI cricket with 491/4."
    elif re.search(r'\b(who has the most catches in women\'s odi cricket)\b', user_input):
        return "Charlotte Edwards has the most catches in women's ODI cricket."
    elif re.search(r'\b(who has the most runs in a single women\'s t20 world cup)\b', user_input):
        return "Beth Mooney scored the most runs in a single women's T20 World Cup with 259 runs in 2020."
    elif re.search(r'\b(who has the most runs in a single women\'s odi world cup)\b', user_input):
        return "Debbie Hockley scored the most runs in a single women's ODI World Cup with 456 runs in 1997."
    elif re.search(r'\b(who has the most matches as captain in women\'s international cricket)\b', user_input):
        return "Charlotte Edwards has captained the most matches in women's international cricket."
    elif re.search(r'\b(who has the most stumpings in women\'s t20 cricket)\b', user_input):
        return "Alyssa Healy holds the record for the most stumpings in women's T20 international cricket."
    elif re.search(r'\b(what is the highest individual score in women\'s t20 cricket)\b', user_input):
        return "Meg Lanning holds the highest individual score in women's T20 international cricket with 133 not out."
    elif re.search(r'\b(who has the most ducks in women\'s odi cricket)\b', user_input):
        return "Anisa Mohammed holds the record for the most ducks in women's ODI cricket."
    elif re.search(r'\b(who has the most five-wicket hauls in women\'s t20 cricket)\b', user_input):
        return "Anisa Mohammed holds the record for the most five-wicket hauls in women's T20 international cricket."
    elif re.search(r'\b(what is the fastest fifty in women\'s odi cricket)\b', user_input):
        return "Deandra Dottin holds the record for the fastest fifty in women's ODI cricket, scored in 22 balls."
    elif re.search(r'\b(who has the most catches in women\'s t20 cricket)\b', user_input):
        return "Sophie Devine holds the record for the most catches in women's T20 international cricket."
    else:
        # Default response for unknown queries
        return "I'm sorry, I don't have the answer to that question. Can you please ask something else?"

# Main loop to keep the chatbot running
def main():
    print("ChatBot: Hello! You can ask me questions about cricket. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()