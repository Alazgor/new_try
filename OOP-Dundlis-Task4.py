class ShoppingCart:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return bool(self.items)

    def __repr__(self):
        return f"ShoppingCart({self.items})"

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Shopping Cart: {len(self.items)} items"

    def __contains__(self, item):
        return item in self.items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Item not found in the shopping cart.")

# Example usage:
cart = ShoppingCart()
cart.add_item("Laptop")
cart.add_item("Phone")
cart.add_item("Headphones")

print(bool(cart))          # Output: True
print(len(cart))           # Output: 3
print(str(cart))           # Output: Shopping Cart: 3 items
print(repr(cart))          # Output: ShoppingCart(['Laptop', 'Phone', 'Headphones'])
print("Phone" in cart)     # Output: True

cart.remove_item("Phone")
print("Phone" in cart)     # Output: False


class Post:
    def __init__(self, content, likes=0):
        self.content = content
        self.likes = likes

    def __repr__(self):
        return f"Post({self.content}, likes={self.likes})"

    def __str__(self):
        return f"Post: '{self.content}' - Likes: {self.likes}"

    def __eq__(self, other):
        return self.content == other.content

    def like(self):
        self.likes += 1

# Example usage:
post1 = Post("This is my first post!")
post2 = Post("This is my first post!")

print(post1 == post2)      # Output: True

post1.like()
post1.like()
print(post1)               # Output: Post: 'This is my first post!' - Likes: 2

class Playlist:
    def __init__(self):
        self.tracks = []

    def __repr__(self):
        return f"Playlist({self.tracks})"

    def __str__(self):
        return f"Playlist: {len(self.tracks)} tracks"

    def __len__(self):
        return len(self.tracks)

    def __getitem__(self, index):
        return self.tracks[index]

    def add_track(self, track):
        self.tracks.append(track)

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
        else:
            print("Track not found in the playlist.")

# Example usage:
playlist = Playlist()
playlist.add_track("Song 1")
playlist.add_track("Song 2")
playlist.add_track("Song 3")

print(len(playlist))       # Output: 3
print(playlist)            # Output: Playlist: 3 tracks
print(repr(playlist))      # Output: Playlist(['Song 1', 'Song 2', 'Song 3'])

playlist.remove_track("Song 2")
print(len(playlist))       # Output: 2
