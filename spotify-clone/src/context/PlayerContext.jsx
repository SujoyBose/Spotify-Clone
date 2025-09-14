import { createContext, useEffect, useRef, useState } from "react";
import axios from "axios";

export const PlayerContext = createContext();

const PlayerContextProvider = (props) => {
    const audioRef = useRef();

    // player seek bar 
    const seekBg = useRef();
    const seekBar = useRef();

    // ⚠️ Change this to your real backend port (5173 is Vite frontend)
    const url = "http://localhost:4000";

    // state
    const [songsData, setSongsData] = useState([]);
    const [albumData, setAlbumData] = useState([]);
    const [track, setTrack] = useState(null); // start with null
    const [playerStatus, setPlayerStatus] = useState(false);
    const [time, setTime] = useState({
        currentTime: { second: 0, minute: 0 },
        totalTime: { second: 0, minute: 0 }
    });

    // play or pause
    const play = () => {
        if (audioRef.current) {
            audioRef.current.play();
            setPlayerStatus(true);
        }
    };

    const pause = () => {
        if (audioRef.current) {
            audioRef.current.pause();
            setPlayerStatus(false);
        }
    };

    const playWithId = async (id) => {
        await songsData.map((item) => {
            if (id === item._id) {
                setTrack(item);
            }
        })

        await audioRef.current.play();
        setPlayStatus(true);
    }


    const previous = async () => {
        songsData.map(async (item, index) => {
            if (track._id === item._id && index > 0) {
                await setTrack(songsData[index - 1]);
                await audioRef.current.play();
                setPlayStatus(true);
            }
        })
    };


    const next = async () => {
        songsData.map(async (item, index) => {
            if (track._id === item._id && index < songsData.length ) {
                await setTrack(songsData[index + 1]);
                await audioRef.current.play();
                setPlayStatus(true);
            }
        })
    };

    const seekSong = (e) => {
        if (audioRef.current && seekBg.current) {
            audioRef.current.currentTime =
                (e.nativeEvent.offsetX / seekBg.current.offsetWidth) *
                audioRef.current.duration;
        }
    };

    // fetch songs
    const getSongsData = async () => {
        try {
            const response = await axios.get(`${url}/api/song/list`);
            console.log("Songs API response:", response.data);

            // API may return { songs: [...] } or just [...]
            const songs = response.data.songs || response.data;
            setSongsData(songs);

            if (songs.length > 0) {
                setTrack(songs[0]);
            }
        } catch (error) {
            console.error("Error fetching songs:", error);
        }
    };

    // fetch albums
    const getAlbumData = async () => {
        try {
            const response = await axios.get(`${url}/api/album/list`);
            console.log("Albums API response:", response.data);

            const albums = response.data.albums || response.data;
            setAlbumData(albums);
        } catch (error) {
            console.error("Error fetching albums:", error);
        }
    };

    // update seek bar + time
    useEffect(() => {
        if (!audioRef.current) return;

        audioRef.current.ontimeupdate = () => {
            if (!audioRef.current.duration) return;

            // update seek bar
            if (seekBar.current) {
                seekBar.current.style.width =
                    Math.floor(
                        (audioRef.current.currentTime /
                            audioRef.current.duration) *
                        100
                    ) + "%";
            }

            // update time
            setTime({
                currentTime: {
                    second: Math.floor(audioRef.current.currentTime % 60),
                    minute: Math.floor(audioRef.current.currentTime / 60)
                },
                totalTime: {
                    second: Math.floor(audioRef.current.duration % 60),
                    minute: Math.floor(audioRef.current.duration / 60)
                }
            });
        };
    }, []);

    // fetch songs + albums on mount
    useEffect(() => {
        getSongsData();
        getAlbumData();
    }, []);

    const contextValue = {
        audioRef,
        seekBg,
        seekBar,
        track,
        setTrack,
        playerStatus,
        setPlayerStatus,
        time,
        setTime,
        play,
        pause,
        playWithId,
        previous,
        next,
        seekSong,
        songsData,
        albumData
    };

    return (
        <PlayerContext.Provider value={contextValue}>
            {props.children}
        </PlayerContext.Provider>
    );
};

export default PlayerContextProvider;
