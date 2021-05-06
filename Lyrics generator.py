''' This would allow the user to choose from a list of songs and then get the lyrics to
that song. '''

'''
Lyrics generator

Ask a user to choose from a list of 10 songs. When the user does, you print out the lyrics to the song they selected.

Example:

Welcome, please select a select a song from this top 10 songs:

1. Baby by Bieber
2. Hotline Bling by Drake
3. Flawless by Beyonce
4. Fall by Eminem...

You chose Flawless by Beyonce. Here you go:

------- Flawless by Beyonce ------------
I'm out that H, town coming coming down
I'm coming down, drippin' candy on the ground
H, Town, Town, I'm coming down, coming down
Drippin' candy on the ground...

Press * to choose again.

To push it further, have at least 3 songs by the same artist.

Next, ask the user to put the name of the artist so you can show them only options by that artist. Then the user can select a specific song from that list.
'''

#Pseudocode
''' 1) Print text : Welcome
    2) Take input from the user
    3) Use the input to a dict (number maps to the lyrics)
    4) Print the lyrics
'''

if __name__ == '__main__':
    list = [[1, 'We Have Overcome by Rivers and Robots'], [2, 'In Control by Hillsong Worship'],
            [3, 'Waterfall by Jonathan Ogden'] , [4, 'While I Wait by Lincoln Brewster']]  #Songs list

    print("Welcome, please select a select a song from these top 4 songs:\n" ) #First message the user sees
    for number, song in list: #tuple unpacking
        print(f"{number} : {song}") #printing the elements from the list
    print("\n")

    while True:
        try:
            options = int(input())
        except:
            options = -1

        if options > 0 and options < 5:
            print("\n")
            break
        else:
            print("Please select a select a song from the the list:")
            continue

    lyrics = { 1 :  '''     We Have Overcome
                            We are purified
                            We are hidden in the wounds of Christ
                            He has paid the price
                            He has brought us near
                            To behold the glory of The Lord
                            So we will not fear
                            Through the storm and through the flood
                            By Your spirit, by Your blood
                            We will stand, we will stand
                            And with a trumpet call
                            You will open up the sky
                            Come with glory and with might
                            And we will be with the Lamb
                            Hallelujah,
                            Hallelujah,
                            We will be with You
                            Though the storm may come
                            We are unashamed
                            Of the name above all other names
                            He's our victory
                            He's our joy and prize
                            He's the reason we lay down our lives ''' ,


                    2 : ''' From heaven You can hear
                            I know You're drawing near
                            As I worship
                            Held within Your love
                            The wind and waves will come
                            But I will stay here
                            I lift my hands to heaven
                            Hear my heart surrender
                            I tell my soul again
                            You are Lord of all
                            And though the seas are raging
                            You will speak and tame them
                            In You I find my rest
                            You are in control
                            Through valleys I will trust
                            Your Spirit is enough
                            To keep me walking
                            You guide my every step
                            Speak life to me again
                            Lord I need You
                            Oh, I need You
                            I lift my hands to heaven
                            Hear my heart surrender
                            I tell my soul again
                            You are Lord of all
                            And though the seas are raging
                            You will speak and tame them
                            In You I find my rest
                            You are in control
                            I will trust in only You
                            No one can add to Your perfection
                            You're the beginning and the end
                            More than I can comprehend
                            There is no one like You
                            No one
                            I will trust in only You
                            No one can add to Your perfection
                            You're the beginning and the end
                            More than I can comprehend
                            There is no one like You
                            No one
                            I will trust in only You
                            No one can add to Your perfection
                            You're the beginning and the end
                            More than I can comprehend
                            There is no one like You Jesus
                            I lift my hands to heaven
                            Hear my heart surrender
                            I tell my soul again
                            You are Lord of all
                            And though the seas are raging
                            You will speak and tame them
                            In You I find my rest
                            You are in control
                            I lift my hands to heaven
                            Hear my heart surrender
                            I tell my soul again
                            You are Lord of all
                            And though the seas are raging
                            You will speak and tame them
                            In You I find my rest
                            You are in control
                            In You I find my rest
                            You are in control ''' ,

                    3 : ''' Everlasting One
                            Nothing else compares
                            To knowing You
                            To knowing You
                            You're the living God
                            And my soul it longs
                            To be with You
                            To be with You
                            Oh Lord Your love is like a waterfall
                            Your love is like a flowing stream
                            And whenever I'm feeling dry
                            I come to the river, I come to the river of life
                            You are worthy Lord
                            Of every song that I could sing
                            That I could sing
                            And my heart cries out
                            God I need You more than anything
                            Than anything
                            'Cause Your love is like a waterfall
                            Your love is like a flowing stream
                            And whenever I'm feeling dry
                            I come to the river, I come to the river of life
                            Oh, come to the river of life
                            As the deer pants for the waters
                            So my soul longs after You
                            As the deer pants for the waters
                            So my soul longs after You
                            As the deer pants for the waters
                            So my soul longs after You
                            As the deer pants for the waters
                            So my soul longs after You ''' ,

                    4 : ''' Deep within my heart, I know You've won
                            I know You've overcome
                            And even in the dark, when I'm undone
                            I still believe it
                            I live by faith, and not by sight
                            Sometimes miracles take time
                            While I wait, I will worship
                            Lord, I'll worship Your name
                            While I wait, I will trust You
                            Lord, I'll trust You all the same
                            When I fall apart, You are my strength
                            Help me not forget
                            Seeing every scar, You make me whole
                            You're my healer
                            I live by faith, and not by sight
                            Sometimes miracles take time
                            I live by faith, and not by sight
                            Sometimes miracles take time
                            While I wait, I will worship
                            Lord, I'll worship Your name
                            While I wait, I will trust You
                            Lord, I'll trust You all the same
                            You're faithful every day
                            Your promises remain
                            You're faithful every day
                            Your promises remain
                            You're faithful every day
                            Your promises remain
                            You're faithful every day
                            Your promises remain
                            Though I don't understand it
                            I will worship with my pain
                            You are God, You are worthy
                            You are with me all the way
                            So while I wait, I will worship
                            Lord, I'll worship Your name
                            Though I don't have all the answers
                            Still I trust You all the same ''' } #lyrics to the songs


    for number, song in list: #iterate through the list and get the right song
        if options == number:
            print(f"You chose {song}. Here you go:\n")
            print(f"------- {song} ------------", lyrics.get(options))


''' To do: Format print output properly. '''
