import pyautogui
import time

# List of educative sentences
educative_sentences = [
    "Scamming others for money is not only unethical but also illegal.",
    "Using your skills for good can lead to a much more fulfilling life than scamming people.",
    "Consider the harm you're causing to innocent people by engaging in scams.",
    "There are many legitimate ways to earn money that do not involve deceit.",
    "By scamming people, you are creating a cycle of mistrust and negativity.",
    "You have the potential to make a positive impact on the world; scamming does not achieve that.",
    "Honest work may be harder, but it is far more rewarding in the long run.",
    "Think about how you would feel if someone scammed your family or friends.",
    "Scamming can lead to severe legal consequences, including jail time.",
    "You can choose to use your intelligence and skills to help others instead of harming them.",
    "Building a career based on honesty and integrity will earn you respect and trust.",
    "There are many organizations that can help you find legitimate work opportunities.",
    "Consider seeking help if you feel trapped in the cycle of scamming.",
    "Think about the long-term consequences of your actions, not just the short-term gains.",
    "Scamming ruins lives; it is not a victimless crime.",
    "You are capable of much more than just scamming people.",
    "Using your talents for good can bring you real satisfaction and pride.",
    "There are many online courses that can help you learn new skills and find honest work.",
    "Imagine the positive change you could make by choosing a different path.",
    "It's never too late to start doing the right thing and make amends for your actions.",
    "Scamming others for money is not only unethical but also illegal.",
    "Using your skills for good can lead to a much more fulfilling life than scamming people.",
    "Consider the harm you're causing to innocent people by engaging in scams.",
    "There are many legitimate ways to earn money that do not involve deceit.",
    "By scamming people, you are creating a cycle of mistrust and negativity.",
    "You have the potential to make a positive impact on the world; scamming does not achieve that.",
    "Honest work may be harder, but it is far more rewarding in the long run.",
    "Think about how you would feel if someone scammed your family or friends.",
    "Scamming can lead to severe legal consequences, including jail time.",
    "You can choose to use your intelligence and skills to help others instead of harming them.",
    "Building a career based on honesty and integrity will earn you respect and trust.",
    "There are many organizations that can help you find legitimate work opportunities.",
    "Consider seeking help if you feel trapped in the cycle of scamming.",
    "Think about the long-term consequences of your actions, not just the short-term gains.",
    "Scamming ruins lives; it is not a victimless crime.",
    "You are capable of much more than just scamming people.",
    "Using your talents for good can bring you real satisfaction and pride.",
    "There are many online courses that can help you learn new skills and find honest work.",
    "Imagine the positive change you could make by choosing a different path.",
    "It's never too late to start doing the right thing and make amends for your actions.",
    "By choosing honesty, you can build a better future for yourself and others.",
    "Engaging in scams destroys trust, which is hard to rebuild.",
    "Consider the impact of your actions on your own conscience and peace of mind.",
    "There are countless opportunities to make a positive impact; scamming isn't one of them.",
    "Think about the example you're setting for others by engaging in scams.",
    "A life of integrity is more valuable than any amount of money gained through deceit.",
    "Each day is a new chance to make the right choices and change your path.",
    "Real success comes from hard work and perseverance, not from taking advantage of others.",
    "Your actions today shape your future; choose a path you can be proud of.",
    "Consider the satisfaction of earning respect through honest means.",
    "You can achieve great things without resorting to unethical behavior.",
    "Think about the kind of world you want to live in and contribute to making it better.",
    "You have the power to change your life for the better by making ethical choices.",
    "Scamming might bring short-term gains, but it results in long-term losses.",
    "Honesty is the foundation of trust and meaningful relationships.",
    "The skills you use for scams can be redirected to legitimate and rewarding opportunities.",
    "Consider the legacy you want to leave behind; scamming won't be a proud part of it."
]

# Time to switch to the application where you want to type the messages
time.sleep(5)  # 5 seconds delay to switch to the target application

# Type each sentence with a delay between them
for sentence in educative_sentences:
    pyautogui.typewrite(sentence)
    pyautogui.press('enter')  # Press Enter to send the message
    time.sleep(1)  # Wait for 1 second before sending the next message
