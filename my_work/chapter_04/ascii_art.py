# Challenge for Chapter 4 of the Python Essentials Training Course on LinkedIn Learning
# Encodes strings of ASCII characters and decodes them back to original state

def encodeString(stringVal):
    """
    Encodes a string using run-length encoding.

    Parameters:
        stringVal (str): The input string to be encoded.
    
    Returns:
        list: A list of tuples where each tuple contains a character and its count.
    """
    # Initialize an empty list to store encoded data
    encoded = []
    
    # Initialize variables to track the previous character and its count
    prevChar = None
    count = 0

    # Iterate through the input string, character by character
    for char in stringVal:
        if char != prevChar:
            # If the current character is different from the previous one,
            # append the previous character and its count to the encoded list
            if prevChar is not None:
                encoded.append((prevChar, count))
            # Update prevChar to the current character and reset count
            prevChar = char
            count = 1
        else:
            # If the current character is the same as the previous one,
            # increment the count
            count += 1

    # Append the last character and its count to the encoded list
    if prevChar is not None:
        encoded.append((prevChar, count))

    # Return the encoded list of tuples
    return encoded

def decodeString(encodedList):
    """
    Decodes a run-length encoded list back into the original string.

    Parameters:
        encodedList (list): A list of tuples where each tuple contains a character and its count.
    
    Returns:
        str: The original string reconstructed from the encoded list.
    """
    # Initialize an empty string to store the decoded data
    decoded = ''
    
    # Iterate through each tuple in the encoded list
    for tup in encodedList:
        # Multiply the character by its count and add it to the decoded string
        decoded += tup[0] * tup[1]
    
    # Return the decoded string
    return decoded

# ASCII art string to be encoded and decoded
art = '''
                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                
'''

# Encode the ASCII art
encoded = encodeString(art)

# Decode the encoded ASCII art back to its original form
decoded = decodeString(encoded)
