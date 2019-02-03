import sqlite3
conn = sqlite3.connect('/home/pi/reader.db')

print('module version', sqlite3.version)
print('sqlite version', sqlite3.sqlite_version)
print('conn', conn)

c = conn.cursor()

ursula = "It exists... It's real. I can call it a misunderstanding, but I can't pretend that it doesn't exist, or will ever cease to exist. Suffering is the condition on which we live. And when it comes, you know it. You know it as the truth. Of course it's right to cure diseases, to prevent hunger and injustice, as the social organism does. But no society can change the nature of existence. We can't prevent suffering. This pain and that pain, yes, but not Pain. A society can only relieve social suffering, unnecessary suffering. The rest remains. The root, the reality. All of us here are going to know grief; if we live fifty years, we'll have known pain for fifty years... And yet, I wonder if it isn't all a misunderstanding - this grasping after happiness, this fear of pain... If instead of fearing it and running from it, one could... get through it, go beyond it. There is something beyond it. It's the self that suffers, and there's a place where the self-ceases. I don't know how to say it. But I believe that the reality - the truth that I recognize in suffering as I don't in comfort and happiness - that the reality of pain is not pain. If you can get through it. If you can endure it all the way."

c.execute("INSERT INTO books VALUES ('Ursula Test', 'It exists... Its real. I can call it a misunderstanding, but I cant pretend that it doesnt exist, or will ever cease to exist. Suffering is the condition on which we live. And when it comes, you know it. You know it as the truth. Of course its right to cure diseases, to prevent hunger and injustice, as the social organism does. But no society can change the nature of existence. We cant prevent suffering. This pain and that pain, yes, but not Pain. A society can only relieve social suffering, unnecessary suffering. The rest remains. The root, the reality. All of us here are going to know grief; if we live fifty years, well have known pain for fifty years... And yet, I wonder if it isnt all a misunderstanding - this grasping after happiness, this fear of pain... If instead of fearing it and running from it, one could... get through it, go beyond it. There is something beyond it. Its the self that suffers, and theres a place where the self-ceases. I dont know how to say it. But I believe that the reality - the truth that I recognize in suffering as I dont in comfort and happiness - that the reality of pain is not pain. If you can get through it. If you can endure it all the way.')")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
