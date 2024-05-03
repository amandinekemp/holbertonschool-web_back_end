#!/usr/bin/env python3
"""
pagination - 3. Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
	def __init__(self):
   		self.__dataset = None
    	self.__indexed_dataset = None

	def dataset(self) -> List[List]:
		"""Returns a cached dataset"""
		if self.__dataset is None:
			with open(self.DATA_FILE) as f:
				reader = csv.reader(f)
				dataset = [row for row in reader]
			self.__dataset = dataset[1:]

		return self.__dataset

	def indexed_dataset(self) -> Dict[int, List]:
		"""Returns a dataset indexed by sorting position, starting at 0"""
		if self.__indexed_dataset is None:
			dataset = self.dataset()
			truncated_dataset = dataset[:1000]
			self.__indexed_dataset = {
				i: dataset[i] for i in range(len(dataset))
			}
		return self.__indexed_dataset

	def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
		"""Returns a dictionary of pagination data

		Args:
			index (int, optional): The starting index. Defaults to None.
			page_size (int, optional): The size of the page. Defaults to 10.

		Returns:
			Dict: A dictionary of pagination data
		"""
		# Retrieve the total count of items in the indexed dataset
		total_items = len(self.indexed_dataset())

		# Verify whether the specified index is present in the indexed dataset
		if index is not None and index not in self.indexed_dataset():
			# If the specified index is not present,locate the next available index
			next_index = index + 1
			while next_index < total_items and \
					next_index not in self.indexed_dataset():
				next_index += 1

			# Set the start index to the next available index
			start_index = next_index

		else:
			# Use the given index, or start from the beginning if none is provided
			start_index = index if index is not None else 0

		# Compute the ending index for the current page
		end_index = min(start_index + page_size, total_items)

		# Retrieve the data for the current page
		data = [self.indexed_dataset()[i] for i in range(
			start_index, end_index)]

		# Determine the next index to use for querying
		next_index = end_index if end_index < total_items else None

		# Create and return the result dictionary
		result = {
			'index': start_index,
			'next_index': next_index,
			'page_size': page_size,
			'data': data,
		}

		return result
