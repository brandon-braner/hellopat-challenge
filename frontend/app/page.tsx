'use client';

import { useState, useEffect } from 'react';
import { v4 as uuidv4 } from 'uuid';

type Message = {
  role: 'user' | 'assistant';
  content: string;
};

type User = {
  id: string;
  name: string;
};

const apiUrl = process.env.NEXT_PUBLIC_API_URL;

export default function Home() {
  const [user, setUser] = useState<User | null>(null);
  const [sessionId, setSessionId] = useState<string>('');
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // Fetch user data
    fetch(`${apiUrl}/users/me`)
      .then((res) => res.json())
      .then((data) => setUser(data))
      .catch((error) => {
        console.error('Error fetching user:', error);
        setError('Failed to load user data. Please try refreshing the page.');
      });

    // Generate or retrieve session ID
    const storedSessionId = localStorage.getItem('chatSessionId');
    if (storedSessionId) {
      setSessionId(storedSessionId);
    } else {
      const newSessionId = uuidv4();
      setSessionId(newSessionId);
      localStorage.setItem('chatSessionId', newSessionId);
    }

     // Fetch chat history
     fetch(`${apiUrl}/chat/get_chat_history/${storedSessionId}`)
     .then((res) => res.json())
     .then((data) => {
        data.forEach((item: any) => {
          const messageArray = JSON.parse(item['message']);
          const message: Message = {
            role: messageArray['type'] === 'human' ? 'user' : 'assistant',
            content: messageArray['data']['content']
          }
          setMessages((prevMessages) => [...prevMessages, message]);
        });
     })
     .catch((error: any) => {
       console.error('Error fetching chat history:', error);
       setError('Failed to load chat history. Please try refreshing the page.');
     });
  }, []);

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;
    setIsLoading(true);
    setError(null);
    const newMessage: Message = { role: 'user', content: input };
    setMessages((prev) => [...prev, newMessage]);
    setInput('');

    try {
      const response = await fetch(`${apiUrl}/chat/product_recommendation`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_input: input,
          session_id: sessionId,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to send message');
      }

      const data = await response.json();
      const assistantMessage: Message = { role: 'assistant', content: data.response };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      setError('Failed to send message. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-6">
      <div className="w-full max-w-2xl flex flex-col space-y-4">
        <div className="bg-white rounded-lg shadow p-4 mb-4">
          {user ? `Hello, ${user.name}!` : 'Loading user...'}
        </div>
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <span className="block sm:inline">{error}</span>
          </div>
        )}
        <div className="flex-1 overflow-y-auto space-y-4 mb-4 h-96">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`p-3 rounded-lg ${
                message.role === 'user' ? 'bg-blue-700 ml-auto text-white text-right' : 'bg-gray-100 text-black'
              }`}
            >
              {message.content}
            </div>
          ))}
          {isLoading && (
            <div className="text-center">
              <span className="inline-block animate-spin rounded-full h-8 w-8 border-t-2 border-b-2 border-gray-900 text-black"></span>
            </div>
          )}
        </div>
        <div className="flex space-x-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            className="flex-1 p-2 border rounded-lg text-black "
            placeholder="Type your message..."
            disabled={isLoading}
          />
          <button
            onClick={sendMessage}
            className={`px-4 py-2 bg-blue-500 text-white rounded-lg ${isLoading ? 'opacity-50 cursor-not-allowed' : ''}`}
            disabled={isLoading}
          >
            Send
          </button>
        </div>
      </div>
    </main>
  );

}