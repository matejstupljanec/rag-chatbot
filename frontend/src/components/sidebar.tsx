import { useEffect, useState } from "react";

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;

interface Conversation {
  id: number;
  name: string;
  user_id: number;
  created_at: string;
  updated_at: string;
}

export default function Sidebar() {
  const [conversations, setConversations] = useState<Conversation[]>([]);
  const [currentConversation, setCurrentConversation] =
    useState<Conversation>();

  async function getConversations() {
    const response = await fetch(`${apiBaseUrl}/api/conversations`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });

    const conversations = await response.json();

    setConversations(conversations);
  }

  async function createConversation() {
    const response = await fetch(`${apiBaseUrl}/api/conversations`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({}),
    });

    const conversation = await response.json();

    getConversations();
    setCurrentConversation(conversation);
  }

  useEffect(() => {
    getConversations();
  }, []);

  useEffect(() => {
    if (conversations.length > 0) {
      setCurrentConversation(conversations[0]);
    }
  }, [conversations]);

  return (
    <div className="flex flex-col w-3xs h-dvh p-2 bg-darkblue text-white">
      <div className="text-center text-3xl">FERKO</div>
      <div className="flex flex-col flex-1 min-h-0">
        <div className="mt-5 mb-5">
          <button
            className="flex flex-row items-center p-2 w-full hover:bg-lightblue rounded-xl cursor-pointer"
            onClick={createConversation}
          >
            <div className="w-5.5 h-5.5">
              <svg
                width="100%"
                height="100%"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12 8V16M8 12H16M22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12Z"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </div>
            <div className="text-xl ml-2">Novi razgovor</div>
          </button>
        </div>
        <div className="w-full flex flex-col flex-1 min-h-0">
          <div className="w-full p-2 text-lg">
            <span className="border-b pb-1 opacity-60">Nedavni razgovori</span>
          </div>
          <ul className="w-full text-lg overflow-y-auto scrollbar scrollbar-thumb-gray-600 scrollbar-track-gray-600">
            {conversations.map((conversation) => (
              <li
                key={conversation.id}
                onClick={() => {
                  setCurrentConversation(conversation);
                }}
                className={`p-2 pt-1 pb-1 mb-1 w-full rounded-xl select-none cursor-pointer ${currentConversation && conversation.id === currentConversation.id ? "bg-lightblue" : "hover:bg-lightblue"}`}
              >
                {conversation.name}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}
