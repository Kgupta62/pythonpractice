tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]
# tuples=[t for t in tuples if t]
# tuples= filter(None, tuples)
tuples = [t for i, t in enumerate(tuples) if t]
print(tuples)
