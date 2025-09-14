import mongoose from "mongoose";

const songSchema = new mongoose.Schema({
  name:     { type: String, required: true },
  desc:     { type: String, required: true },
  album:    { type: String, required: true },
  image:    { type: String, required: true },
  file:     { type: String, required: true },
  duration: { type: String, required: true }
});

// look in mongoose.models first, otherwise create it
const songModel =
  mongoose.models.Song ||               // already compiled?
  mongoose.model('Song', songSchema);   // compile it once

export default songModel;
