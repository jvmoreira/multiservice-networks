import React, { ReactElement, useEffect } from 'react';
import { StateUpdater } from '@/commons/change-handler';
import { useNfvTeFunctionParameters } from '@/commons/nfv-te-values';
import { TokenBucketShaperIntervalField } from './token-bucket-shaper-interval-field';
import { TokenBucketShaperBucketSizeField } from './token-bucket-shaper-bucket-size-field';
import { TokenBucketShaperMaxSizeField } from './token-bucket-shaper-max-size-field';
import { TokenBucketShaperRateField } from './token-bucket-shaper-rate-field';
import { TokenBucketShaperQueueMaxSizeField } from './token-bucket-shaper-queue-max-size-field';

type TokenBucketShaperParameters = {
  rate: string,
  bucket_size: string,
  bucket_max_size: string,
  interval: string,
  queue_max_size: string,
};

export function TokenBucketShaperParameters(): ReactElement {
  const [
    tokenBucketShaperParameters,
    setTokenBucketShaperParameters,
  ] = useNfvTeFunctionParameters<TokenBucketShaperParameters>();

  useSetTokenBucketShaperInitialParameters(setTokenBucketShaperParameters);

  return (
    <>
      <TokenBucketShaperBucketSizeField
        tokenBucketShaperParameters={tokenBucketShaperParameters}
        setTokenBucketShaperParameters={setTokenBucketShaperParameters}
      />

      <TokenBucketShaperMaxSizeField
        tokenBucketShaperParameters={tokenBucketShaperParameters}
        setTokenBucketShaperParameters={setTokenBucketShaperParameters}
      />

      <TokenBucketShaperIntervalField
        tokenBucketShaperParameters={tokenBucketShaperParameters}
        setTokenBucketShaperParameters={setTokenBucketShaperParameters}
      />

      <TokenBucketShaperRateField
        tokenBucketShaperParameters={tokenBucketShaperParameters}
        setTokenBucketShaperParameters={setTokenBucketShaperParameters}
      />

      <TokenBucketShaperQueueMaxSizeField
        tokenBucketShaperParameters={tokenBucketShaperParameters}
        setTokenBucketShaperParameters={setTokenBucketShaperParameters}
      />
    </>
  );
}

export interface TokenBucketShaperParameterFieldProps {
  tokenBucketShaperParameters: TokenBucketShaperParameters,
  setTokenBucketShaperParameters: StateUpdater<TokenBucketShaperParameters>,
}

function useSetTokenBucketShaperInitialParameters(
  setTokenBucketShaperParameters: StateUpdater<TokenBucketShaperParameters>,
): void {
  useEffect(() => {
    setTokenBucketShaperParameters({
      rate: '',
      bucket_size: '',
      bucket_max_size: '',
      interval: '',
      queue_max_size: '',
    });
  }, [setTokenBucketShaperParameters]);
}
