const Sentiment = require("sentiment");
const axios = require("axios");
const sentiment = new Sentiment();

async function indexData(data) {
  try {
    data.sentiment = sentiment.analyze(data.text).score;
    const response = await axios.post(
      "http://localhost:9200/index_name/doc_type",
      data
    );
    console.log(`Data successfully indexed with ID: ${response.data._id}`);
  } catch (error) {
    console.error(error);
  }
}

stream.on("tweet", (tweet) => {
  console.log(tweet.text);
  indexData({
    text: tweet.text,
    user: tweet.user.screen_name,
    created_at: tweet.created_at,
  });
});
