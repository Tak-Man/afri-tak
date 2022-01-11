import afr_utils as utils
import json


if __name__ == "__main__":
    # Test get_stop_words()
    # ------------------------------------------------------------------------------------------------------
    stop_words = utils.get_stop_words(json_file="./word2vec_af_wikipedia.json",
                                      number_of_stop_words=None,
                                      word_count_threshold=0.35,
                                      remove_punctuation=True,
                                      lowercase_words=True)

    print("stop_words :", stop_words)
    print("len(stop_words) :", len(stop_words))

    with open("./package/stop_words.txt", "w") as outfile:
        json.dump(stop_words, outfile)
    # ------------------------------------------------------------------------------------------------------