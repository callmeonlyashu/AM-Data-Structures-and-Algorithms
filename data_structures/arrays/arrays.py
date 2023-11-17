#!/usr/bin/env python
# coding: utf-8

# In[13]:


class AshuList:
    
    def __init__(self, size):
        import random
        self.data = []
        for index in range(size):
            self.data.append(None)
            
    def get_actual_length(self):
        count = 0
        for i in range(len(self.data)):
            if self.data[i] is not None:
                count+=1
            else:
                break
        
        return count
    def traverse(self, jump=0):
        '''
        Returns the updated traversed list with the jumps specified.

        Parameters:
                jump (int): Jump indexes during traversal

        Returns:
                new_list (List): List of traversed list elements
        '''
        counter = 0
        new_list = []
        for index in range(len(self.data)):
            counter += 1
            if counter > jump:
                new_list.append(self.data[index])
                counter=0
        
        return new_list
    
    def insert(self, index, value, shift=True):
        '''
        Returns the updated traversed list with added elements.

        Parameters:
                index (int): Index where you want to insert the value
                value (int): Value which you want to insert
                shift (bool): If index contains a value then shift all elements or not.

        Returns:
                new_list (List): List of traversed list elements
        '''
        
        actual_length = self.get_actual_length()
        
        # Check if there is space to insert
        if None not in self.data:
            return "No Place to insert/shift"
        
        # When inserting at location far from last inserted.
        if index > actual_length:
            self.data[actual_length] = value
            return self.data
        
        #Inserting at None
        if self.data[index] is None:
            self.data[index] = value
            return self.data
        else:
            #Inserting at Not None
            # When shifting is enabled
            shift_start_point=actual_length-1
            if shift==True:
                if self.data[index] is not None:
                     while shift_start_point>=index:
                            """Old Swapping code"""
#                             self.data[shift_start_point], self.data[shift_start_point+1] = \
#                             self.data[shift_start_point-1], self.data[shift_start_point]
                            """Optimized Code"""
                            self.data[shift_start_point+1] = self.data[shift_start_point]
                            shift_start_point-=1

                self.data[index]=value
            else:
            # When shifting is disabled
                self.data[actual_length]=self.data[index]
                self.data[index]=value
            
            return self.data
    
    def delete(self, index, shift=True):
        '''
        Returns the updated traversed list with deleted elements.

        Parameters:
                index (int): Index where you want to insert the value
                shift (bool): If index contains a value then shift all elements or not.

        Returns:
                new_list (List): List of traversed list elements
        '''
        
        actual_length = self.get_actual_length()
        
        #Deleting at not None
        if self.data[index] is None:
            del self.data[index]
            return self.data
        else:
            # Deleting at Not None
            # When shifting is enabled
            shift_start_point=index
            shift_stop_point=actual_length
            if shift==True:
                if self.data[index] is not None:
                     while shift_start_point>=actual_length:
                            """Old Swapping code"""
#                             self.data[shift_start_point-1], self.data[shift_start_point] = \
#                             self.data[shift_start_point], self.data[shift_start_point+1]
                            """Optimized code"""
                            self.data[shift_start_point-1] = self.data[shift_start_point] 
                            shift_start_point+=1

                del self.data[index]
            else:
            # When shifting is disabled
                self.data[actual_length]=self.data[index]
                del self.data[index]
            
            return self.data




