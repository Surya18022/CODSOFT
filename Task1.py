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
        return "Virat Kohli has the most runs in T20 international
