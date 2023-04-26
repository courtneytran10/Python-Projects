def main():
 #------------------------------------------------------------------------ 
 print("Record Of Ragnarok: 10 Strongest Characters, Ranked\n")
# Define the parallel arrays
 import time
 characters = ["Lu Bu", "Adam", "Thor", "Poseidon", "Shiva", "Kojiro Sasaki", "Jack The Ripper", "Zeus", "Raiden Tameemon", "Hercules"]
 strengths = [68, 85, 95, 81, 92, 82, 75, 98, 89, 80]
# Ask the user if they want to see the full ranking
 show_full_ranking = input("Do you want to see the full ranking? (y/n) ")
 if show_full_ranking.lower() == "y":
# Sort the characters and strengths arrays in descending order by strength
# key=lambda is used to specify a function that takes an element as input and returns a value that is used for sorting
# sorted() function sorts the list of strengths 
# key parameter specifies a function of one argument to extract a comparison key from each element in the iterable
  sorted_indices = sorted(range(len(strengths)), key = lambda idx: strengths[idx], reverse = True)
  sorted_characters = [characters[idx] for idx in sorted_indices]
  sorted_strengths = [strengths[idx] for idx in sorted_indices]
# Display the full ranking
  print("\nFull ranking:\n")
  for idx in range(len(sorted_characters)):
   print(f"{idx+1}. {sorted_characters[idx]} - {sorted_strengths[idx]}\n")
  else:
# Initialize the index of the highest ranking character
   highest_rank_index = 0
# Loop through the characters and find the index of the highest ranking character
  for idx in range(1, len(characters)):
   if strengths[idx] > strengths[highest_rank_index]:
    highest_rank_index = idx
# Display the name and strength of the highest ranking character
  time.sleep(1)
  print(f"The strongest God is {characters[highest_rank_index]} with a strength of {strengths[highest_rank_index]}.")
  time.sleep(1)
  print()
  print("The strongest human is Raiden Tameemon with a strength of 89.")
#-------------------------------------------------------------------   
main()
# Option for the user to see the full ranking and to sort the characters and strengths arrays in descending order by strength. The main change is the use of the sorted() function with the key parameter. The key parameter is used to specify a function that takes an element as input and returns a value that is used for sorting. In this case, the key parameter takes a lambda function that returns the strength of the character at the given index. The reverse parameter is set to True to sort the list in descending order.
# The sorted_indices variable holds a list of indices that correspond to the sorted list of strengths. The sorted_characters and sorted_strengths variables are then generated by indexing into the characters and strengths lists using the sorted indices.
#If the user chooses not to see the full ranking, the code will loop through the characters and find the index of the character with the highest strength using a for loop and if statement.