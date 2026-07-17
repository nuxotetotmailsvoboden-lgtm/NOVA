"use client";

import { useQuery } from "@tanstack/react-query";

import { clientsApi } from "../api/clients";

interface UseClientsOptions {
  page?: number;
  pageSize?: number;
  search?: string;
  status?: string;
}

export function useClients(options: UseClientsOptions = {}) {
  return useQuery({
    queryKey: ["clients", options],

    queryFn: async () => {
      const response = await clientsApi.getAll(options);

      return response.data;
    },

    placeholderData: (previousData) => previousData,

    staleTime: 1000 * 60,
  });
}
