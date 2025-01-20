def encodeString(stringVal):
    """
    Encodes a string using run-length encoding.

    Parameters:
        stringVal (str): The input string to be encoded.
    
    Returns:
        list: A list of tuples where each tuple contains a character and its count.
    """
    # Return an empty list if the input string is empty
    if not stringVal:
        return []

    # Initialize the encoded list and the first character
    encoded = []
    prevChar = stringVal[0]
    count = 1

    # Iterate through the string starting from the second character
    for char in stringVal[1:]:
        if char == prevChar:
            # Increment the count if the character is the same as the previous one
            count += 1
        else:
            # Append the previous character and its count to the encoded list
            encoded.append((prevChar, count))
            # Reset for the new character
            prevChar = char
            count = 1

    # Append the last character and its count
    encoded.append((prevChar, count))
    return encoded


def decodeString(encodedList):
    """
    Decodes a run-length encoded list back into the original string.

    Parameters:
        encodedList (list): A list of tuples where each tuple contains a character and its count.
    
    Returns:
        str: The original string reconstructed from the encoded list.
    """
    # Use a generator expression to construct the decoded string efficiently
    return ''.join(char * count for char, count in encodedList)


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

# Verify correctness and print the decoded art
assert art == decoded, "The decoded art does not match the original!"
print("Round-trip encoding and decoding succeeded!")
