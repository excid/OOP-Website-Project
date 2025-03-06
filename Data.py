import Class

platform = Class.Platform()
sample_account = Class.Account("example@example.com", "password123", "John Doe", "johndoe")
sample_account.edit_data(
    "example@example.com",
    "John Doe",
    "1234567890",
    ["USA", "123 Main St", "Apt 4B", "Suburb", "New York", "NY", "10001"],
)
platform.add_account(sample_account)

account = platform.search_account("example@example.com")