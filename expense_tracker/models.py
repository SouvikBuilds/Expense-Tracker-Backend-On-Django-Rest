from mongoengine import Document, StringField, DecimalField

class ExpenseModel(Document):
    CHOICE_CATEGORY = [
        ('F', 'FOOD'),
        ('T', 'TRAVEL'),
        ('E', "ENTERTAINMENT"),
        ('S', "SPORTS"),
        ('O', "OTHERS")
    ]
    
    title = StringField(max_length=100, required=True)
    amount = DecimalField(precision=2, required=True)
    category = StringField(max_length=2, choices=CHOICE_CATEGORY, required=True)

    meta = {
        'collection': 'expenses'  # This will be the collection name in MongoDB
    }

    def __str__(self):
        return f"{self.title} - {self.amount}"