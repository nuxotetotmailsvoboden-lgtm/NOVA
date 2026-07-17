"use client";

import { useQuery } from "@tanstack/react-query";

import { clientsApi } from "../api/clients";

export function useClient(id: string) {
  return useQuery({
    queryKey: ["client", id],

    queryFn: async () => {
      const response = await clientsApi.getById(id);

      return response.data;
    },

    enabled: Boolean(id),

    staleTime: 1000 * 60,
  });
}
