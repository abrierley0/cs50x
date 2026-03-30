// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("File did not open correctly\n");
        return false;
    }

    // Read each word in the file

    // Declare the string
    char word[LENGTH + 1];

    // Read each word one by one until end of the file
    while (fgets(word, LENGTH, source) != NULL)
    {
        // Create space for new hash table node
        node *hashnode = malloc(sizeof(node));

        // Copy word into the new node
        strcpy(hashnode->word, word);

        // Hash the word to obtain its hash value
        int hashvalue = hash(word);

        // Insert the new node into the hash table
        hashnode->next = table[hashvalue];   // prepend
        table[hashvalue] = hashnode;    // make new node the first node
    }

    // Close the dictionary file
    fclose(source);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
