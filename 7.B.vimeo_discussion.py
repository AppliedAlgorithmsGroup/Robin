
import pandas as pd

def main():
    clips = pd.read_csv('clips.csv')
    clips.head()
    clips.shape
    clips['1_public'] = (clips['privacy'] == 'anybody')
    print(clips.shape)
    clips.head()
    clips['2_like_play'] = ((clips['total_likes'] > 10) & (clips['total_plays'] > 200))
    print(clips.shape)
    clips.head()
    clips['3_under30'] = (pd.Series(clips['title'].str.len()) < 30)
    print(clips.shape)
    clips.head()
    clips['valid'] = (clips['1_public'] & clips['2_like_play'] & clips['3_under30'])
    clips.head()
    valid = clips[clips['valid']]
    print(valid.shape)
    valid.head()
    invalid = clips[~ clips['valid']]
    print(invalid.shape)
    invalid.head(n=20)
    valid['id'].to_csv("valid.csv",index=False)
    invalid['id'].to_csv("invalid.csv",index=False)


if __name__ == "__main__":
    main()
